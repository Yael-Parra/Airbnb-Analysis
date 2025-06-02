# AirBnB Data Merger Script
# Merges multiple CSV/Excel files into a single manageable file

import pandas as pd
import os
import glob
from pathlib import Path

def merge_airbnb_files(data_directory="data/", output_file="airbnb_complete.csv"):
    """
    Merges all CSV and Excel files from a directory into a single file.
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
    final_df = pd.concat(dataframes_list, ignore_index=True, sort=False)
    
    # Create output directory if it doesn't exist
    output_dir = Path(output_file).parent
    os.makedirs(output_dir, exist_ok=True)
    
    # Save result
    print(f"💾 Guardando en {output_file}...")
    final_df.to_csv(output_file, index=False)
    
    # Compress if too large
    file_size_mb = os.path.getsize(output_file) / (1024 * 1024)
    
    if file_size_mb > 25:  # If larger than 25MB, compress
        compressed_file = output_file.replace('.csv', '.csv.gz')
        print(f"🗜️ Archivo grande ({file_size_mb:.1f}MB), comprimiendo...")
        final_df.to_csv(compressed_file, index=False, compression='gzip')
        print(f"✅ Guardado comprimido: {compressed_file}")
    
    print(f"\n🎉 ¡Completado!")
    print(f"📊 Resultado: {len(final_df)} filas, {len(final_df.columns)} columnas")
    print(f"🌍 Ciudades: {final_df['city'].nunique()}")
    print(f"📁 Archivo: {output_file}")
    
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
    
    print("\n🔍 First 3 rows:")
    print(dataframe.head(3).to_string())

if __name__ == "__main__":
    # Execute the script
    print("🏢 Script de Unión de Datos AirBnB")
    print("=" * 40)
    
    # Change these parameters as needed
    data_dir = "data/"  # Folder where your files are
    output_filename = "processed_data/airbnb_complete.csv"
    
    # Create directories if they don't exist
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs("processed_data", exist_ok=True)
    
    # Merge files
    merged_df = merge_airbnb_files(data_dir, output_filename)
    
    if merged_df is not None:
        # Show preview
        show_data_preview(merged_df)
        
        print("\n📋 Próximos pasos:")
        print("1. Sube el archivo CSV a tu repositorio de GitHub")
        print("2. Usa la URL raw del archivo en Google Colab")
        print("3. ¡Empieza tu análisis exploratorio!")
    else:
        print("\n❌ No se pudieron procesar los datos")
        print("Asegúrate de que los archivos estén en la carpeta 'data/'")