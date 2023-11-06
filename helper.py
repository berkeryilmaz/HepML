import os


def getGasRatio(gas_type):
    molecules = {
        'CH4': 0.0,
        'Ar': 0.0,
        'N2': 0.0,
        'CO2': 0.0,
        'C': 0.0,
        'O': 0.0,
        'H': 0.0
    }

    if (gas_type == 'p10'):
        molecules = {
            'CH4': 0.10,
            'Ar': 0.90,
            'N2': 0.0,
            'CO2': 0.0,
            'C': 0.10 * 0.2,
            'O': 0.0,
            'H': 0.10 * 0.8
        }

    if (gas_type == 'p20'):
        molecules = {
            'CH4': 0.20,
            'Ar': 0.80,
            'N2': 0.0,
            'CO2': 0.0,
            'C': 0.20 * 0.2,
            'O': 0.0,
            'H': 0.20 * 0.8
        }

    if (gas_type == 'arnco2'):
        molecules = {
            'CH4': 0.0,
            'Ar': 0.05,
            'N2': 0.35,
            'CO2': 0.60,
            'C': 0.60 * 0.33,
            'O': 0.60 * 0.67,
            'H': 0.0
        }

    molecules = {molecule: round(ratio,2) for molecule, ratio in molecules.items()}
    return molecules


def createMeasureParams(folder_path):
    gas_type = folder_path[1]
    detector_shape = folder_path[2]
    detector_size = round(float(folder_path[3].replace('kare ', '').replace(',', '.').split('x')[0]), 2)
    detector_area = round(detector_size ** 2, 2)
    cover_size = round(float(folder_path[4].replace('kare ', '').replace(',', '.').split('x')[0]), 2)
    cover_area = round(cover_size ** 2, 2)
    area_ratio = round(cover_area / detector_area, 2)
    gas_ratios = getGasRatio(gas_type)
    voltage = int(folder_path[5].replace('p10 ', '').replace('p20 ', '').split(' ')[0].replace('v', ''))
    source = folder_path[5].replace(gas_type+' ','').split(' ')[1]

    return {
        'Gas_Type': gas_type,
        'CH4': gas_ratios['CH4'],
        'Ar': gas_ratios['Ar'],
        'N2': gas_ratios['N2'],
        'CO2': gas_ratios['CO2'],
        'C': gas_ratios['C'],
        'O': gas_ratios['O'],
        'H': gas_ratios['H'],
        'Shape': detector_shape,
        'Detector_Size': detector_size,
        'Detector_Area': detector_area,
        'Cover_Size': cover_size,
        'Cover_Area': cover_area,
        'Cover_Area_Ratio': area_ratio,
        'Voltage': voltage,
        'Source': source,
        'Time_Window': 0,
        'Peak_Count': 0,
    }


def getOrderedFileList(root):
    file_list = [file for file in os.listdir(root) if file.endswith('.bin')]
    ordered_file_list = sorted(file_list, key=lambda x: int(x.split('.')[0]))
    return ordered_file_list
