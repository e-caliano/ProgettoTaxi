import pandas as pd
from datetime import datetime
import os
import pathlib
import datetime
import time
import platform

dict_lookup = {'LocationID': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 20: 21, 21: 22, 22: 23, 23: 24, 24: 25, 25: 26, 26: 27, 27: 28, 28: 29, 29: 30, 30: 31, 31: 32, 32: 33, 33: 34, 34: 35, 35: 36, 36: 37, 37: 38, 38: 39, 39: 40, 40: 41, 41: 42, 42: 43, 43: 44, 44: 45, 45: 46, 46: 47, 47: 48, 48: 49, 49: 50, 50: 51, 51: 52, 52: 53, 53: 54, 54: 55, 55: 56, 56: 57, 57: 58, 58: 59, 59: 60, 60: 61, 61: 62, 62: 63, 63: 64, 64: 65, 65: 66, 66: 67, 67: 68, 68: 69, 69: 70, 70: 71, 71: 72, 72: 73, 73: 74, 74: 75, 75: 76, 76: 77, 77: 78, 78: 79, 79: 80, 80: 81, 81: 82, 82: 83, 83: 84, 84: 85, 85: 86, 86: 87, 87: 88, 88: 89, 89: 90, 90: 91, 91: 92, 92: 93, 93: 94, 94: 95, 95: 96, 96: 97, 97: 98, 98: 99, 99: 100, 100: 101, 101: 102, 102: 103, 103: 104, 104: 105, 105: 106, 106: 107, 107: 108, 108: 109, 109: 110, 110: 111, 111: 112, 112: 113, 113: 114, 114: 115, 115: 116, 116: 117, 117: 118, 118: 119, 119: 120, 120: 121, 121: 122, 122: 123, 123: 124, 124: 125, 125: 126, 126: 127, 127: 128, 128: 129, 129: 130, 130: 131, 131: 132, 132: 133, 133: 134, 134: 135, 135: 136, 136: 137, 137: 138, 138: 139, 139: 140, 140: 141, 141: 142, 142: 143, 143: 144, 144: 145, 145: 146, 146: 147, 147: 148, 148: 149, 149: 150, 150: 151, 151: 152, 152: 153, 153: 154, 154: 155, 155: 156, 156: 157, 157: 158, 158: 159, 159: 160, 160: 161, 161: 162, 162: 163, 163: 164, 164: 165, 165: 166, 166: 167, 167: 168, 168: 169, 169: 170, 170: 171, 171: 172, 172: 173, 173: 174, 174: 175, 175: 176, 176: 177, 177: 178, 178: 179, 179: 180, 180: 181, 181: 182, 182: 183, 183: 184, 184: 185, 185: 186, 186: 187, 187: 188, 188: 189, 189: 190, 190: 191, 191: 192, 192: 193, 193: 194, 194: 195, 195: 196, 196: 197, 197: 198, 198: 199, 199: 200, 200: 201, 201: 202, 202: 203, 203: 204, 204: 205, 205: 206, 206: 207, 207: 208, 208: 209, 209: 210, 210: 211, 211: 212, 212: 213, 213: 214, 214: 215, 215: 216, 216: 217, 217: 218, 218: 219, 219: 220, 220: 221, 221: 222, 222: 223, 223: 224, 224: 225, 225: 226, 226: 227, 227: 228, 228: 229, 229: 230, 230: 231, 231: 232, 232: 233, 233: 234, 234: 235, 235: 236, 236: 237, 237: 238, 238: 239, 239: 240, 240: 241, 241: 242, 242: 243, 243: 244, 244: 245, 245: 246, 246: 247, 247: 248, 248: 249, 249: 250, 250: 251, 251: 252, 252: 253, 253: 254, 254: 255, 255: 256, 256: 257, 257: 258, 258: 259, 259: 260, 260: 261, 261: 262, 262: 263, 263: 264, 264: 265}, 'Borough': {0: 'EWR', 1: 'Queens', 2: 'Bronx', 3: 'Manhattan', 4: 'Staten Island', 5: 'Staten Island', 6: 'Queens', 7: 'Queens', 8: 'Queens', 9: 'Queens', 10: 'Brooklyn', 11: 'Manhattan', 12: 'Manhattan', 13: 'Brooklyn', 14: 'Queens', 15: 'Queens', 16: 'Brooklyn', 17: 'Bronx', 18: 'Queens', 19: 'Bronx', 20: 'Brooklyn', 21: 'Brooklyn', 22: 'Staten Island', 23: 'Manhattan', 24: 'Brooklyn', 25: 'Brooklyn', 26: 'Queens', 27: 'Queens', 28: 'Brooklyn', 29: 'Queens', 30: 'Bronx', 31: 'Bronx', 32: 'Brooklyn', 33: 'Brooklyn', 34: 'Brooklyn', 35: 'Brooklyn', 36: 'Brooklyn', 37: 'Queens', 38: 'Brooklyn', 39: 'Brooklyn', 40: 'Manhattan', 41: 'Manhattan', 42: 'Manhattan', 43: 'Staten Island', 44: 'Manhattan', 45: 'Bronx', 46: 'Bronx', 47: 'Manhattan', 48: 'Brooklyn', 49: 'Manhattan', 50: 'Bronx', 51: 'Brooklyn', 52: 'Queens', 53: 'Brooklyn', 54: 'Brooklyn', 55: 'Queens', 56: 'Queens', 57: 'Bronx', 58: 'Bronx', 59: 'Bronx', 60: 'Brooklyn', 61: 'Brooklyn', 62: 'Brooklyn', 63: 'Queens', 64: 'Brooklyn', 65: 'Brooklyn', 66: 'Brooklyn', 67: 'Manhattan', 68: 'Bronx', 69: 'Queens', 70: 'Brooklyn', 71: 'Brooklyn', 72: 'Queens', 73: 'Manhattan', 74: 'Manhattan', 75: 'Brooklyn', 76: 'Brooklyn', 77: 'Bronx', 78: 'Manhattan', 79: 'Brooklyn', 80: 'Bronx', 81: 'Queens', 82: 'Queens', 83: 'Staten Island', 84: 'Brooklyn', 85: 'Queens', 86: 'Manhattan', 87: 'Manhattan', 88: 'Brooklyn', 89: 'Manhattan', 90: 'Brooklyn', 91: 'Queens', 92: 'Queens', 93: 'Bronx', 94: 'Queens', 95: 'Queens', 96: 'Brooklyn', 97: 'Queens', 98: 'Staten Island', 99: 'Manhattan', 100: 'Queens', 101: 'Queens', 102: 'Manhattan', 103: 'Manhattan', 104: 'Manhattan', 105: 'Brooklyn', 106: 'Manhattan', 107: 'Brooklyn', 108: 'Staten Island', 109: 'Staten Island', 110: 'Brooklyn', 111: 'Brooklyn', 112: 'Manhattan', 113: 'Manhattan', 114: 'Staten Island', 115: 'Manhattan', 116: 'Queens', 117: 'Staten Island', 118: 'Bronx', 119: 'Manhattan', 120: 'Queens', 121: 'Queens', 122: 'Brooklyn', 123: 'Queens', 124: 'Manhattan', 125: 'Bronx', 126: 'Manhattan', 127: 'Manhattan', 128: 'Queens', 129: 'Queens', 130: 'Queens', 131: 'Queens', 132: 'Brooklyn', 133: 'Queens', 134: 'Queens', 135: 'Bronx', 136: 'Manhattan', 137: 'Queens', 138: 'Queens', 139: 'Manhattan', 140: 'Manhattan', 141: 'Manhattan', 142: 'Manhattan', 143: 'Manhattan', 144: 'Queens', 145: 'Queens', 146: 'Bronx', 147: 'Manhattan', 148: 'Brooklyn', 149: 'Brooklyn', 150: 'Manhattan', 151: 'Manhattan', 152: 'Manhattan', 153: 'Brooklyn', 154: 'Brooklyn', 155: 'Staten Island', 156: 'Queens', 157: 'Manhattan', 158: 'Bronx', 159: 'Queens', 160: 'Manhattan', 161: 'Manhattan', 162: 'Manhattan', 163: 'Manhattan', 164: 'Brooklyn', 165: 'Manhattan', 166: 'Bronx', 167: 'Bronx', 168: 'Bronx', 169: 'Manhattan', 170: 'Queens', 171: 'Staten Island', 172: 'Queens', 173: 'Bronx', 174: 'Queens', 175: 'Staten Island', 176: 'Brooklyn', 177: 'Brooklyn', 178: 'Queens', 179: 'Queens', 180: 'Brooklyn', 181: 'Bronx', 182: 'Bronx', 183: 'Bronx', 184: 'Bronx', 185: 'Manhattan', 186: 'Staten Island', 187: 'Brooklyn', 188: 'Brooklyn', 189: 'Brooklyn', 190: 'Queens', 191: 'Queens', 192: 'Queens', 193: 'Manhattan', 194: 'Brooklyn', 195: 'Queens', 196: 'Queens', 197: 'Queens', 198: 'Bronx', 199: 'Bronx', 200: 'Queens', 201: 'Manhattan', 202: 'Queens', 203: 'Staten Island', 204: 'Queens', 205: 'Staten Island', 206: 'Queens', 207: 'Bronx', 208: 'Manhattan', 209: 'Brooklyn', 210: 'Manhattan', 211: 'Bronx', 212: 'Bronx', 213: 'Staten Island', 214: 'Queens', 215: 'Queens', 216: 'Brooklyn', 217: 'Queens', 218: 'Queens', 219: 'Bronx', 220: 'Staten Island', 221: 'Brooklyn', 222: 'Queens', 223: 'Manhattan', 224: 'Brooklyn', 225: 'Queens', 226: 'Brooklyn', 227: 'Brooklyn', 228: 'Manhattan', 229: 'Manhattan', 230: 'Manhattan', 231: 'Manhattan', 232: 'Manhattan', 233: 'Manhattan', 234: 'Bronx', 235: 'Manhattan', 236: 'Manhattan', 237: 'Manhattan', 238: 'Manhattan', 239: 'Bronx', 240: 'Bronx', 241: 'Bronx', 242: 'Manhattan', 243: 'Manhattan', 244: 'Staten Island', 245: 'Manhattan', 246: 'Bronx', 247: 'Bronx', 248: 'Manhattan', 249: 'Bronx', 250: 'Staten Island', 251: 'Queens', 252: 'Queens', 253: 'Bronx', 254: 'Brooklyn', 255: 'Brooklyn', 256: 'Brooklyn', 257: 'Queens', 258: 'Bronx', 259: 'Queens', 260: 'Manhattan', 261: 'Manhattan', 262: 'Manhattan', 263: 'Unknown', 264: 'Unknown'}, 'Zone': {0: 'Newark Airport', 1: 'Jamaica Bay', 2: 'Allerton/Pelham Gardens', 3: 'Alphabet City', 4: 'Arden Heights', 5: 'Arrochar/Fort Wadsworth', 6: 'Astoria', 7: 'Astoria Park', 8: 'Auburndale', 9: 'Baisley Park', 10: 'Bath Beach', 11: 'Battery Park', 12: 'Battery Park City', 13: 'Bay Ridge', 14: 'Bay Terrace/Fort Totten', 15: 'Bayside', 16: 'Bedford', 17: 'Bedford Park', 18: 'Bellerose', 19: 'Belmont', 20: 'Bensonhurst East', 21: 'Bensonhurst West', 22: 'Bloomfield/Emerson Hill', 23: 'Bloomingdale', 24: 'Boerum Hill', 25: 'Borough Park', 26: 'Breezy Point/Fort Tilden/Riis Beach', 27: 'Briarwood/Jamaica Hills', 28: 'Brighton Beach', 29: 'Broad Channel', 30: 'Bronx Park', 31: 'Bronxdale', 32: 'Brooklyn Heights', 33: 'Brooklyn Navy Yard', 34: 'Brownsville', 35: 'Bushwick North', 36: 'Bushwick South', 37: 'Cambria Heights', 38: 'Canarsie', 39: 'Carroll Gardens', 40: 'Central Harlem', 41: 'Central Harlem North', 42: 'Central Park', 43: 'Charleston/Tottenville', 44: 'Chinatown', 45: 'City Island', 46: 'Claremont/Bathgate', 47: 'Clinton East', 48: 'Clinton Hill', 49: 'Clinton West', 50: 'Co-Op City', 51: 'Cobble Hill', 52: 'College Point', 53: 'Columbia Street', 54: 'Coney Island', 55: 'Corona', 56: 'Corona', 57: 'Country Club', 58: 'Crotona Park', 59: 'Crotona Park East', 60: 'Crown Heights North', 61: 'Crown Heights South', 62: 'Cypress Hills', 63: 'Douglaston', 64: 'Downtown Brooklyn/MetroTech', 65: 'DUMBO/Vinegar Hill', 66: 'Dyker Heights', 67: 'East Chelsea', 68: 'East Concourse/Concourse Village', 69: 'East Elmhurst', 70: 'East Flatbush/Farragut', 71: 'East Flatbush/Remsen Village', 72: 'East Flushing', 73: 'East Harlem North', 74: 'East Harlem South', 75: 'East New York', 76: 'East New York/Pennsylvania Avenue', 77: 'East Tremont', 78: 'East Village', 79: 'East Williamsburg', 80: 'Eastchester', 81: 'Elmhurst', 82: 'Elmhurst/Maspeth', 83: "Eltingville/Annadale/Prince's Bay", 84: 'Erasmus', 85: 'Far Rockaway', 86: 'Financial District North', 87: 'Financial District South', 88: 'Flatbush/Ditmas Park', 89: 'Flatiron', 90: 'Flatlands', 91: 'Flushing', 92: 'Flushing Meadows-Corona Park', 93: 'Fordham South', 94: 'Forest Hills', 95: 'Forest Park/Highland Park', 96: 'Fort Greene', 97: 'Fresh Meadows', 98: 'Freshkills Park', 99: 'Garment District', 100: 'Glen Oaks', 101: 'Glendale', 102: "Governor's Island/Ellis Island/Liberty Island", 103: "Governor's Island/Ellis Island/Liberty Island", 104: "Governor's Island/Ellis Island/Liberty Island", 105: 'Gowanus', 106: 'Gramercy', 107: 'Gravesend', 108: 'Great Kills', 109: 'Great Kills Park', 110: 'Green-Wood Cemetery', 111: 'Greenpoint', 112: 'Greenwich Village North', 113: 'Greenwich Village South', 114: 'Grymes Hill/Clifton', 115: 'Hamilton Heights', 116: 'Hammels/Arverne', 117: 'Heartland Village/Todt Hill', 118: 'Highbridge', 119: 'Highbridge Park', 120: 'Hillcrest/Pomonok', 121: 'Hollis', 122: 'Homecrest', 123: 'Howard Beach', 124: 'Hudson Sq', 125: 'Hunts Point', 126: 'Inwood', 127: 'Inwood Hill Park', 128: 'Jackson Heights', 129: 'Jamaica', 130: 'Jamaica Estates', 131: 'JFK Airport', 132: 'Kensington', 133: 'Kew Gardens', 134: 'Kew Gardens Hills', 135: 'Kingsbridge Heights', 136: 'Kips Bay', 137: 'LaGuardia Airport', 138: 'Laurelton', 139: 'Lenox Hill East', 140: 'Lenox Hill West', 141: 'Lincoln Square East', 142: 'Lincoln Square West', 143: 'Little Italy/NoLiTa', 144: 'Long Island City/Hunters Point', 145: 'Long Island City/Queens Plaza', 146: 'Longwood', 147: 'Lower East Side', 148: 'Madison', 149: 'Manhattan Beach', 150: 'Manhattan Valley', 151: 'Manhattanville', 152: 'Marble Hill', 153: 'Marine Park/Floyd Bennett Field', 154: 'Marine Park/Mill Basin', 155: 'Mariners Harbor', 156: 'Maspeth', 157: 'Meatpacking/West Village West', 158: 'Melrose South', 159: 'Middle Village', 160: 'Midtown Center', 161: 'Midtown East', 162: 'Midtown North', 163: 'Midtown South', 164: 'Midwood', 165: 'Morningside Heights', 166: 'Morrisania/Melrose', 167: 'Mott Haven/Port Morris', 168: 'Mount Hope', 169: 'Murray Hill', 170: 'Murray Hill-Queens', 171: 'New Dorp/Midland Beach', 172: 'North Corona', 173: 'Norwood', 174: 'Oakland Gardens', 175: 'Oakwood', 176: 'Ocean Hill', 177: 'Ocean Parkway South', 178: 'Old Astoria', 179: 'Ozone Park', 180: 'Park Slope', 181: 'Parkchester', 182: 'Pelham Bay', 183: 'Pelham Bay Park', 184: 'Pelham Parkway', 185: 'Penn Station/Madison Sq West', 186: 'Port Richmond', 187: 'Prospect-Lefferts Gardens', 188: 'Prospect Heights', 189: 'Prospect Park', 190: 'Queens Village', 191: 'Queensboro Hill', 192: 'Queensbridge/Ravenswood', 193: 'Randalls Island', 194: 'Red Hook', 195: 'Rego Park', 196: 'Richmond Hill', 197: 'Ridgewood', 198: 'Rikers Island', 199: 'Riverdale/North Riverdale/Fieldston', 200: 'Rockaway Park', 201: 'Roosevelt Island', 202: 'Rosedale', 203: 'Rossville/Woodrow', 204: 'Saint Albans', 205: 'Saint George/New Brighton', 206: 'Saint Michaels Cemetery/Woodside', 207: 'Schuylerville/Edgewater Park', 208: 'Seaport', 209: 'Sheepshead Bay', 210: 'SoHo', 211: 'Soundview/Bruckner', 212: 'Soundview/Castle Hill', 213: 'South Beach/Dongan Hills', 214: 'South Jamaica', 215: 'South Ozone Park', 216: 'South Williamsburg', 217: 'Springfield Gardens North', 218: 'Springfield Gardens South', 219: 'Spuyten Duyvil/Kingsbridge', 220: 'Stapleton', 221: 'Starrett City', 222: 'Steinway', 223: 'Stuy Town/Peter Cooper Village', 224: 'Stuyvesant Heights', 225: 'Sunnyside', 226: 'Sunset Park East', 227: 'Sunset Park West', 228: 'Sutton Place/Turtle Bay North', 229: 'Times Sq/Theatre District', 230: 'TriBeCa/Civic Center', 231: 'Two Bridges/Seward Park', 232: 'UN/Turtle Bay South', 233: 'Union Sq', 234: 'University Heights/Morris Heights', 235: 'Upper East Side North', 236: 'Upper East Side South', 237: 'Upper West Side North', 238: 'Upper West Side South', 239: 'Van Cortlandt Park', 240: 'Van Cortlandt Village', 241: 'Van Nest/Morris Park', 242: 'Washington Heights North', 243: 'Washington Heights South', 244: 'West Brighton', 245: 'West Chelsea/Hudson Yards', 246: 'West Concourse', 247: 'West Farms/Bronx River', 248: 'West Village', 249: 'Westchester Village/Unionport', 250: 'Westerleigh', 251: 'Whitestone', 252: 'Willets Point', 253: 'Williamsbridge/Olinville', 254: 'Williamsburg (North Side)', 255: 'Williamsburg (South Side)', 256: 'Windsor Terrace', 257: 'Woodhaven', 258: 'Woodlawn/Wakefield', 259: 'Woodside', 260: 'World Trade Center', 261: 'Yorkville East', 262: 'Yorkville West', 263: 'NV', 264: 'nan'}, 'service_zone': {0: 'EWR', 1: 'Boro Zone', 2: 'Boro Zone', 3: 'Yellow Zone', 4: 'Boro Zone', 5: 'Boro Zone', 6: 'Boro Zone', 7: 'Boro Zone', 8: 'Boro Zone', 9: 'Boro Zone', 10: 'Boro Zone', 11: 'Yellow Zone', 12: 'Yellow Zone', 13: 'Boro Zone', 14: 'Boro Zone', 15: 'Boro Zone', 16: 'Boro Zone', 17: 'Boro Zone', 18: 'Boro Zone', 19: 'Boro Zone', 20: 'Boro Zone', 21: 'Boro Zone', 22: 'Boro Zone', 23: 'Yellow Zone', 24: 'Boro Zone', 25: 'Boro Zone', 26: 'Boro Zone', 27: 'Boro Zone', 28: 'Boro Zone', 29: 'Boro Zone', 30: 'Boro Zone', 31: 'Boro Zone', 32: 'Boro Zone', 33: 'Boro Zone', 34: 'Boro Zone', 35: 'Boro Zone', 36: 'Boro Zone', 37: 'Boro Zone', 38: 'Boro Zone', 39: 'Boro Zone', 40: 'Boro Zone', 41: 'Boro Zone', 42: 'Yellow Zone', 43: 'Boro Zone', 44: 'Yellow Zone', 45: 'Boro Zone', 46: 'Boro Zone', 47: 'Yellow Zone', 48: 'Boro Zone', 49: 'Yellow Zone', 50: 'Boro Zone', 51: 'Boro Zone', 52: 'Boro Zone', 53: 'Boro Zone', 54: 'Boro Zone', 55: 'Boro Zone', 56: 'Boro Zone', 57: 'Boro Zone', 58: 'Boro Zone', 59: 'Boro Zone', 60: 'Boro Zone', 61: 'Boro Zone', 62: 'Boro Zone', 63: 'Boro Zone', 64: 'Boro Zone', 65: 'Boro Zone', 66: 'Boro Zone', 67: 'Yellow Zone', 68: 'Boro Zone', 69: 'Boro Zone', 70: 'Boro Zone', 71: 'Boro Zone', 72: 'Boro Zone', 73: 'Boro Zone', 74: 'Boro Zone', 75: 'Boro Zone', 76: 'Boro Zone', 77: 'Boro Zone', 78: 'Yellow Zone', 79: 'Boro Zone', 80: 'Boro Zone', 81: 'Boro Zone', 82: 'Boro Zone', 83: 'Boro Zone', 84: 'Boro Zone', 85: 'Boro Zone', 86: 'Yellow Zone', 87: 'Yellow Zone', 88: 'Boro Zone', 89: 'Yellow Zone', 90: 'Boro Zone', 91: 'Boro Zone', 92: 'Boro Zone', 93: 'Boro Zone', 94: 'Boro Zone', 95: 'Boro Zone', 96: 'Boro Zone', 97: 'Boro Zone', 98: 'Boro Zone', 99: 'Yellow Zone', 100: 'Boro Zone', 101: 'Boro Zone', 102: 'Yellow Zone', 103: 'Yellow Zone', 104: 'Yellow Zone', 105: 'Boro Zone', 106: 'Yellow Zone', 107: 'Boro Zone', 108: 'Boro Zone', 109: 'Boro Zone', 110: 'Boro Zone', 111: 'Boro Zone', 112: 'Yellow Zone', 113: 'Yellow Zone', 114: 'Boro Zone', 115: 'Boro Zone', 116: 'Boro Zone', 117: 'Boro Zone', 118: 'Boro Zone', 119: 'Boro Zone', 120: 'Boro Zone', 121: 'Boro Zone', 122: 'Boro Zone', 123: 'Boro Zone', 124: 'Yellow Zone', 125: 'Boro Zone', 126: 'Boro Zone', 127: 'Boro Zone', 128: 'Boro Zone', 129: 'Boro Zone', 130: 'Boro Zone', 131: 'Airports', 132: 'Boro Zone', 133: 'Boro Zone', 134: 'Boro Zone', 135: 'Boro Zone', 136: 'Yellow Zone', 137: 'Airports', 138: 'Boro Zone', 139: 'Yellow Zone', 140: 'Yellow Zone', 141: 'Yellow Zone', 142: 'Yellow Zone', 143: 'Yellow Zone', 144: 'Boro Zone', 145: 'Boro Zone', 146: 'Boro Zone', 147: 'Yellow Zone', 148: 'Boro Zone', 149: 'Boro Zone', 150: 'Yellow Zone', 151: 'Boro Zone', 152: 'Boro Zone', 153: 'Boro Zone', 154: 'Boro Zone', 155: 'Boro Zone', 156: 'Boro Zone', 157: 'Yellow Zone', 158: 'Boro Zone', 159: 'Boro Zone', 160: 'Yellow Zone', 161: 'Yellow Zone', 162: 'Yellow Zone', 163: 'Yellow Zone', 164: 'Boro Zone', 165: 'Boro Zone', 166: 'Boro Zone', 167: 'Boro Zone', 168: 'Boro Zone', 169: 'Yellow Zone', 170: 'Boro Zone', 171: 'Boro Zone', 172: 'Boro Zone', 173: 'Boro Zone', 174: 'Boro Zone', 175: 'Boro Zone', 176: 'Boro Zone', 177: 'Boro Zone', 178: 'Boro Zone', 179: 'Boro Zone', 180: 'Boro Zone', 181: 'Boro Zone', 182: 'Boro Zone', 183: 'Boro Zone', 184: 'Boro Zone', 185: 'Yellow Zone', 186: 'Boro Zone', 187: 'Boro Zone', 188: 'Boro Zone', 189: 'Boro Zone', 190: 'Boro Zone', 191: 'Boro Zone', 192: 'Boro Zone', 193: 'Yellow Zone', 194: 'Boro Zone', 195: 'Boro Zone', 196: 'Boro Zone', 197: 'Boro Zone', 198: 'Boro Zone', 199: 'Boro Zone', 200: 'Boro Zone', 201: 'Boro Zone', 202: 'Boro Zone', 203: 'Boro Zone', 204: 'Boro Zone', 205: 'Boro Zone', 206: 'Boro Zone', 207: 'Boro Zone', 208: 'Yellow Zone', 209: 'Boro Zone', 210: 'Yellow Zone', 211: 'Boro Zone', 212: 'Boro Zone', 213: 'Boro Zone', 214: 'Boro Zone', 215: 'Boro Zone', 216: 'Boro Zone', 217: 'Boro Zone', 218: 'Boro Zone', 219: 'Boro Zone', 220: 'Boro Zone', 221: 'Boro Zone', 222: 'Boro Zone', 223: 'Yellow Zone', 224: 'Boro Zone', 225: 'Boro Zone', 226: 'Boro Zone', 227: 'Boro Zone', 228: 'Yellow Zone', 229: 'Yellow Zone', 230: 'Yellow Zone', 231: 'Yellow Zone', 232: 'Yellow Zone', 233: 'Yellow Zone', 234: 'Boro Zone', 235: 'Yellow Zone', 236: 'Yellow Zone', 237: 'Yellow Zone', 238: 'Yellow Zone', 239: 'Boro Zone', 240: 'Boro Zone', 241: 'Boro Zone', 242: 'Boro Zone', 243: 'Boro Zone', 244: 'Boro Zone', 245: 'Yellow Zone', 246: 'Boro Zone', 247: 'Boro Zone', 248: 'Yellow Zone', 249: 'Boro Zone', 250: 'Boro Zone', 251: 'Boro Zone', 252: 'Boro Zone', 253: 'Boro Zone', 254: 'Boro Zone', 255: 'Boro Zone', 256: 'Boro Zone', 257: 'Boro Zone', 258: 'Boro Zone', 259: 'Boro Zone', 260: 'Yellow Zone', 261: 'Yellow Zone', 262: 'Yellow Zone', 263: 'nan', 264: 'nan'}}
df_lookup = pd.DataFrame(dict_lookup)


#df_lookup = pd.read_csv('/Users/edoardocaliano/Desktop/PrgettoTaxi/Data/taxi+_zone_lookup.csv')

# def path_lookup():
#     percorso_lookup = input("Digita il path del file taxi_zone_lookup: ")
#     return percorso_lookup


def load_file(path):
    """
    Funzione per la lettura dei file .parquet o .csv e creazione del dataframe
    :param path: str
    :return: dataframe
    """
    #percorso_lookup = input("Digita il path del file taxi_zone_lookup: ")
    #df_lookup = pd.read_csv('/Users/edoardocaliano/Desktop/PrgettoTaxi/Data/taxi+_zone_lookup.csv')
    #df_lookup = pd.read_csv(percorso_lookup)

    # estrazione dell'estensione del file
    extension = path.split(".")[-1]

    if extension == "csv":
        # se l'estensione è csv, carichiamo il DataFrame dal file CSV
        df = pd.read_csv(path)
    elif extension == "parquet":
        # se l'estensione è parquet, carichiamo il DataFrame dal file PARQUET
        df = pd.read_parquet(path, engine='pyarrow')
    else:
        # se l'estensione non è supportata, solleviamo un'eccezione
        raise ValueError("Estensione del file non supportata. Sono supportati solo i file CSV e PARQUET.")

    return df


def merge(df):
    """
    Funzione per unire il dataframe yellow_tripdata con il dataframe lookup
    :param df: dataframe
    :return: dataframe
    """
    df_lookup
    # percorso_lookup = path_lookup()
    # df_lookup = pd.read_csv(percorso_lookup)

    # rinominazione delle series id di entrambi i dataframe
    df.rename(columns={
        "VendorID": "id"
    }, inplace=True)
    df_lookup.rename(columns={
        "LocationID": "id",
        "Borough": "borough"
    }, inplace=True)

    # facciamo un merge dei due dataframe collegandoli grazie ai rispettivi id in comune
    df_total = pd.merge(left=df, right=df_lookup, on="id")
    # creazione del dataframe di interesse per i calcoli sui tragitti
    df = df_total[["id", "borough", "tpep_pickup_datetime", "tpep_dropoff_datetime"]]

    return df


def filter(df):
    """
    Funzione per il filtraggio del dataframe totale: eliminazione dei valori duplicati e delle righe con valori nulli
    :param df: dataframe
    :return: dataframe
    """
    df = df.drop_duplicates()
    df = df.dropna(subset=['id', 'borough', 'tpep_pickup_datetime', 'tpep_dropoff_datetime'])

    return df


def durata(df):
    """
    Funzione per trovare la durata di ogni corsa
    :param df: dataframe
    :return: dataframe
    """
    # convertiamo le colonne delle date in oggetti datetime
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    # calcoliamo la durata di ogni corsa in secondi
    df['durata_corsa'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds()

    df = df[df['durata_corsa'] > 0]
    return df


def viaggio_più_breve(df):
    """
    :param df: dataframe
    :return: riga del dataframe
    """

    # troviamo l'indice della riga che contiene il valore minimo della serie
    indice_riga_minimo = df["durata_corsa"].idxmin()

    # selezioniamo la riga del dataframe che contiene il valore minimo
    riga_minimo = df.loc[indice_riga_minimo]

    return riga_minimo


def viaggio_più_lungo(df):
    """
    :param df: dataframe
    :return: riga del dataframe
    """

    # troviamo l'indice della riga che contiene il valore massimo della serie
    indice_riga_massimo = df["durata_corsa"].idxmax()

    # selezioniamo la riga del dataframe che contiene il valore massimo
    riga_massimo = df.loc[indice_riga_massimo]

    return riga_massimo



