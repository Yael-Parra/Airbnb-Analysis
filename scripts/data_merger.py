# AirBnB Data Merger Script
# Merges multiple CSV/Excel files into a single manageable file
# Includes duplicate detection and removal

import pandas as pd
import os
import glob
from pathlib import Path

def clean_duplicates(df, id_column=None):
    """
    Cleans duplicate records from the dataframe.
    
    Args:
        df: DataFrame to clean
        id_column: Column name to use as unique identifier (e.g., 'id', 'listing_id')
                  If None, uses all columns to detect duplicates
    
    Returns:
        Cleaned DataFrame and statistics
    """
    print("\n🧹 Iniciando limpieza de duplicados...")
    original_count = len(df)
    
    # Try to identify the ID column automatically if not provided
    if id_column is None:
        potential_id_cols = ['id', 'listing_id', 'property_id', 'airbnb_id']
        for col in potential_id_cols:
            if col in df.columns:
                id_column = col
                print(f"   📋 Usando columna '{id_column}' como identificador único")
                break
    
    if id_column and id_column in df.columns:
        # Remove duplicates based on ID column
        duplicates_mask = df.duplicated(subset=[id_column], keep='first')
        duplicates_count = duplicates_mask.sum()
        
        if duplicates_count > 0:
            print(f"   🔍 Encontrados {duplicates_count} duplicados basados en '{id_column}'")
            df_clean = df[~duplicates_mask].copy()
        else:
            print(f"   ✅ No se encontraron duplicados basados en '{id_column}'")
            df_clean = df.copy()
    else:
        # Remove completely identical rows
        print("   📋 No se encontró columna ID, removiendo filas completamente idénticas")
        duplicates_count = df.duplicated().sum()
        
        if duplicates_count > 0:
            print(f"   🔍 Encontrados {duplicates_count} duplicados completos")
            df_clean = df.drop_duplicates().copy()
        else:
            print("   ✅ No se encontraron filas completamente duplicadas")
            df_clean = df.copy()
    
    final_count = len(df_clean)
    removed_count = original_count - final_count
    
    print(f"   📊 Filas originales: {original_count:,}")
    print(f"   📊 Filas después de limpieza: {final_count:,}")
    print(f"   📊 Duplicados removidos: {removed_count:,}")
    
    return df_clean, {
        'original_count': original_count,
        'final_count': final_count,
        'duplicates_removed': removed_count
    }

def basic_data_cleaning(df):
    """
    Performs basic data cleaning operations.
    
    Args:
        df: DataFrame to clean
    
    Returns:
        Cleaned DataFrame and cleaning statistics
    """
    print("\n🔧 Realizando limpieza básica de datos...")
    
    cleaning_stats = {}
    
    # Remove completely empty rows
    empty_rows_before = df.isnull().all(axis=1).sum()
    if empty_rows_before > 0:
        df = df.dropna(how='all')
        print(f"   🗑️ Removidas {empty_rows_before} filas completamente vacías")
    
    # Clean whitespace in string columns
    string_columns = df.select_dtypes(include=['object']).columns
    for col in string_columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()
    
    print(f"   ✨ Limpiados espacios en blanco en {len(string_columns)} columnas de texto")
    
    # Basic statistics
    cleaning_stats['empty_rows_removed'] = empty_rows_before
    cleaning_stats['string_columns_cleaned'] = len(string_columns)
    
    return df, cleaning_stats

def merge_airbnb_files(data_directory="data/", output_file="airbnb_complete.csv", id_column=None):
    """
    Merges all CSV and Excel files from a directory into a single file.
    Includes duplicate removal and basic cleaning.
    
    Args:
        data_directory: Directory containing the files to merge
        output_file: Output filename for the merged data
        id_column: Column name to use for duplicate detection (auto-detected if None)
    """
    print("🔍 Buscando archivos de datos...")
    
    # Find CSV and Excel files
    csv_files = glob.glob(os.path.join(data_directory, "*.csv"))
    excel_files = glob.glob(os.path.join(data_directory, "*.xlsx")) + glob.glob(os.path.join(data_directory, "*.xls"))
    
    all_files = csv_files + excel_files
    
    if not all_files:
        print(f"❌ No se encontraron archivos en {data_directory}")
        return None
    
    print(f"📁 Encontrados {len(all_files)} archivos:")
    for file_path in all_files:
        print(f"   - {os.path.basename(file_path)}")
    
    # Load and combine files
    dataframes_list = []
    total_raw_rows = 0
    
    for file_path in all_files:
        print(f"📖 Cargando {os.path.basename(file_path)}...")
        
        try:
            # Load based on extension
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            else:  # Excel
                df = pd.read_excel(file_path)
            
            # Add column with filename/city
            file_name = Path(file_path).stem
            df['city'] = file_name.replace('_', ' ').replace('-', ' ').title()
            
            dataframes_list.append(df)
            total_raw_rows += len(df)
            print(f"   ✅ {len(df)} filas cargadas")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            continue
    
    if not dataframes_list:
        print("❌ No se pudo cargar ningún archivo")
        return None
    
    # Check that all have the same columns
    print("\n🔍 Verificando columnas...")
    reference_columns = set(dataframes_list[0].columns)
    
    for i, df in enumerate(dataframes_list[1:], 1):
        current_columns = set(df.columns)
        if current_columns != reference_columns:
            print(f"⚠️ Archivo {all_files[i]} tiene columnas diferentes")
            print(f"   Faltan: {reference_columns - current_columns}")
            print(f"   Extras: {current_columns - reference_columns}")
    
    # Combine all DataFrames
    print("\n🔗 Combinando datos...")
    combined_df = pd.concat(dataframes_list, ignore_index=True, sort=False)
    print(f"   📊 Total filas combinadas: {len(combined_df):,}")
    
    # Clean duplicates
    cleaned_df, duplicate_stats = clean_duplicates(combined_df, id_column)
    
    # Basic data cleaning
    final_df, cleaning_stats = basic_data_cleaning(cleaned_df)
    
    # Create output directory if it doesn't exist
    output_dir = Path(output_file).parent
    os.makedirs(output_dir, exist_ok=True)
    
    # Save result
    print(f"\n💾 Guardando en {output_file}...")
    final_df.to_csv(output_file, index=False)
    
    # Compress if too large
    file_size_mb = os.path.getsize(output_file) / (1024 * 1024)
    
    if file_size_mb > 25:  # If larger than 25MB, compress
        compressed_file = output_file.replace('.csv', '.csv.gz')
        print(f"🗜️ Archivo grande ({file_size_mb:.1f}MB), comprimiendo...")
        final_df.to_csv(compressed_file, index=False, compression='gzip')
        print(f"✅ Guardado comprimido: {compressed_file}")
    
    # Summary statistics
    print(f"\n🎉 ¡Completado!")
    print("=" * 50)
    print("📊 RESUMEN DE PROCESAMIENTO")
    print("=" * 50)
    print(f"Archivos procesados: {len(all_files)}")
    print(f"Filas originales totales: {total_raw_rows:,}")
    print(f"Duplicados removidos: {duplicate_stats['duplicates_removed']:,}")
    print(f"Filas vacías removidas: {cleaning_stats['empty_rows_removed']:,}")
    print(f"Filas finales: {len(final_df):,}")
    print(f"Columnas: {len(final_df.columns)}")
    print(f"Ciudades: {final_df['city'].nunique()}")
    print(f"Archivo final: {output_file}")
    print(f"Tamaño: {file_size_mb:.1f}MB")
    
    return final_df

def show_data_preview(dataframe):
    """
    Shows a quick preview of the merged data
    """
    print("\n" + "="*50)
    print("📊 PREVIEW DE DATOS")
    print("="*50)
    
    print(f"Total rows: {len(dataframe):,}")
    print(f"Total columns: {len(dataframe.columns)}")
    print(f"Cities: {dataframe['city'].nunique()}")
    
    print("\n🏙️ Rows per city:")
    city_counts = dataframe['city'].value_counts()
    for city, count in city_counts.items():
        print(f"   {city}: {count:,}")
    
    print("\n📋 Column names:")
    for i, col in enumerate(dataframe.columns, 1):
        print(f"   {i:2d}. {col}")
    
    # Check for potential data quality issues
    print("\n🔍 Calidad de datos:")
    missing_data = dataframe.isnull().sum()
    if missing_data.sum() > 0:
        print("   Columnas con datos faltantes:")
        for col, missing_count in missing_data[missing_data > 0].items():
            percentage = (missing_count / len(dataframe)) * 100
            print(f"     {col}: {missing_count:,} ({percentage:.1f}%)")
    else:
        print("   ✅ No hay datos faltantes")
    
    print("\n🔍 Primeras 3 filas:")
    print(dataframe.head(3).to_string())

if __name__ == "__main__":
    # Execute the script
    print("🏢 Script de Unión de Datos AirBnB con Limpieza")
    print("=" * 50)
    
    # Change these parameters as needed
    data_dir = "data/"  # Folder where your files are
    output_filename = "processed_data/airbnb_complete.csv"
    
    # Specify ID column if you know it (e.g., 'id', 'listing_id')
    # Leave as None for auto-detection
    id_column_name = None  # or 'id', 'listing_id', etc.
    
    # Create directories if they don't exist
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs("processed_data", exist_ok=True)
    
    # Merge files with cleaning
    merged_df = merge_airbnb_files(data_dir, output_filename, id_column_name)
    
    if merged_df is not None:
        # Show preview
        show_data_preview(merged_df)
        
        print("\n✅ Merge y limpieza completadas con éxito!")
    else:
        print("\n❌ No se pudieron procesar los datos")
        print("Asegúrate de que los archivos estén en la carpeta 'data/'")