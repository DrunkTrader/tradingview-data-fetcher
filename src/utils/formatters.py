def format_to_csv(data, filename):
    data.to_csv(filename, index=False)

def format_to_json(data, filename):
    data.to_json(filename, orient='records', lines=True)

def format_to_excel(data, filename):
    data.to_excel(filename, index=False)

def format_data(data, output_path, format_type='csv'):
    """
    Format and save the data in the specified format.
    
    Args:
        data: DataFrame containing the trading data
        output_path: Path to save the output file
        format_type: Format type (csv, json, excel)
    """
    if format_type == 'csv':
        data.to_csv(output_path)
    elif format_type == 'json':
        data.to_json(output_path)
    elif format_type == 'excel':
        data.to_excel(output_path)
    else:
        raise ValueError(f"Unsupported format type: {format_type}")