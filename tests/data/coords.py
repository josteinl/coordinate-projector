def getNTM(ntmZone: int):
    for objs in Coords:
        coordSet = Coords[objs]
        print(f"coordSet {coordSet}")
        if coordSet["NTMZONE"] == ntmZone:
            return coordSet


# def getToNTMCoords(transfID,str):


ProjSets = {
    "25832-5105": {"ID": "5", "fromCoord": "UTM32", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25832-5106": {"ID": "6", "fromCoord": "UTM32", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25832-5107": {"ID": "7", "fromCoord": "UTM32", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25832-5108": {"ID": "8", "fromCoord": "UTM32", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25832-5109": {"ID": "9", "fromCoord": "UTM32", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25832-5110": {"ID": "10", "fromCoord": "UTM32", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25832-5111": {"ID": "11", "fromCoord": "UTM32", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25833-5112": {"ID": "12", "fromCoord": "UTM33", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25833-5113": {"ID": "13", "fromCoord": "UTM33", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25833-5114": {"ID": "14", "fromCoord": "UTM33", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25833-5115": {"ID": "15", "fromCoord": "UTM33", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25833-5116": {"ID": "16", "fromCoord": "UTM33", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25833-5117": {"ID": "17", "fromCoord": "UTM33", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25834-5118": {"ID": "18", "fromCoord": "UTM34", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25834-5119": {"ID": "19", "fromCoord": "UTM34", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25834-5120": {"ID": "20", "fromCoord": "UTM34", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25834-5121": {"ID": "21", "fromCoord": "UTM34", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25834-5122": {"ID": "22", "fromCoord": "UTM34", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25834-5123": {"ID": "23", "fromCoord": "UTM34", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25835-5124": {"ID": "24", "fromCoord": "UTM35", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25835-5125": {"ID": "25", "fromCoord": "UTM35", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25835-5126": {"ID": "26", "fromCoord": "UTM35", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25835-5127": {"ID": "27", "fromCoord": "UTM35", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25835-5128": {"ID": "28", "fromCoord": "UTM35", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25835-5129": {"ID": "29", "fromCoord": "UTM35", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25836-5130": {"ID": "30", "fromCoord": "UTM36", "toCoord": "NTM", "expectedAccuracy": 0.00001},
    "25831-23031": {"ID": "36", "fromCoord": "UTM31", "toCoord": "ED50-EPSGIO", "expectedAccuracy": 0.75},
    "25832-23032": {"ID": "37", "fromCoord": "UTM32", "toCoord": "ED50", "expectedAccuracy": 0.75},
    "25833-23033": {"ID": "13", "fromCoord": "UTM33", "toCoord": "ED50-EPSGIO", "expectedAccuracy": 0.75},
    "25834-23034": {"ID": "18", "fromCoord": "UTM34", "toCoord": "ED50-EPSGIO", "expectedAccuracy": 0.75},
    "25835-23035": {"ID": "24", "fromCoord": "UTM35", "toCoord": "ED50-EPSGIO", "expectedAccuracy": 0.75},
    "25836-23036": {"ID": "30", "fromCoord": "UTM36", "toCoord": "ED50-EPSGIO", "expectedAccuracy": 0.75},
    "25830-3857": {"ID": "35", "fromCoord": "UTM30", "toCoord": "3857", "expectedAccuracy": 0.00001},
    "25831-3857": {"ID": "36", "fromCoord": "UTM31", "toCoord": "3857", "expectedAccuracy": 0.00001},
    "25832-3857": {"ID": "37", "fromCoord": "UTM32", "toCoord": "3857", "expectedAccuracy": 0.00001},
    "25833-3857": {"ID": "13", "fromCoord": "UTM33", "toCoord": "3857", "expectedAccuracy": 0.00001},
    "25834-3857": {"ID": "18", "fromCoord": "UTM34", "toCoord": "3857", "expectedAccuracy": 0.00001},
    "25835-3857": {"ID": "24", "fromCoord": "UTM35", "toCoord": "3857", "expectedAccuracy": 0.00001},
    "25836-3857": {"ID": "30", "fromCoord": "UTM36", "toCoord": "3857", "expectedAccuracy": 0.00001},
    "25830-4326": {
        "ID": "35",
        "fromCoord": "UTM30",
        "toCoord": "4326",
        "expectedAccuracy": 0.0000001,
    },  # 0.0000001 is aprox 0.01m (https://www.usna.edu/Users/oceano/pguth/md_help/html/approx_equivalents.htm)
    "25831-4326": {"ID": "36", "fromCoord": "UTM31", "toCoord": "4326", "expectedAccuracy": 0.0000001},
    "25832-4326": {"ID": "37", "fromCoord": "UTM32", "toCoord": "4326", "expectedAccuracy": 0.0000001},
    "25833-4326": {"ID": "13", "fromCoord": "UTM33", "toCoord": "4326", "expectedAccuracy": 0.0000001},
    "25834-4326": {"ID": "18", "fromCoord": "UTM34", "toCoord": "4326", "expectedAccuracy": 0.0000001},
    "25835-4326": {"ID": "24", "fromCoord": "UTM35", "toCoord": "4326", "expectedAccuracy": 0.0000001},
    "25836-4326": {"ID": "30", "fromCoord": "UTM36", "toCoord": "4326", "expectedAccuracy": 0.0000001},
}


Coords = {
    "5": {
        "NTMZONE": 5,
        "UTM": 32,
        "UTM30": [992217.981946, 6571407.602848],
        "UTM31": [648320.774057, 6542585.571617],
        "UTM32": [303655.3945, 6544742.8653],
        "UTM33": [-39991.525312, 6577893],
        "UTM34": [-380771.202566, 6642245.130155],
        "UTM35": [-716664.015939, 6738173.278445],
        "UTM36": [-1045371.96413, 6866165.052239],
        "NTM": [104703.034773, 1111057.611022],
    },
    "6": {
        "NTMZONE": 6,
        "UTM": 32,
        "UTM30": [995868.106627, 6858133.706863],
        "UTM31": [677986.413889, 6827029.739529],
        "UTM32": [359033.278, 6825324.1417],
        "UTM33": [40927.876699, 6853010],
        "UTM34": [-274371.489137, 6910193.138599],
        "UTM35": [-584779.905017, 6997067.673713],
        "UTM36": [-888001.651215, 7113871.570198],
        "NTM": [91934.222867, 1393912.557845],
    },
    "7": {
        "NTMZONE": 7,
        "UTM": 32,
        "UTM30": [1127470.714597, 6505533.65637],
        "UTM31": [776701.714795, 6465108.187314],
        "UTM32": [424563.7735, 6456138.2517],
        "UTM33": [72796.518086, 6478559],
        "UTM34": [-276835.764733, 6532531.295199],
        "UTM35": [-622429.010957, 6618421.2278],
        "UTM36": [-961824.40661, 6736757.311168],
        "NTM": [112636.051453, 1026739.723474],
    },
    "8": {
        "NTMZONE": 8,
        "UTM": 32,
        "UTM30": [1090202.520962, 6983251.424286],
        "UTM31": [783202.699955, 6942521.104181],
        "UTM32": [474403.8687, 6930542.1204],
        "UTM33": [165766.559645, 6947279],
        "UTM34": [-140742.004558, 6992780.803772],
        "UTM35": [-443067.699782, 7067168.963438],
        "UTM36": [-738992.203188, 7170600.446845],
        "NTM": [100157.860489, 1501934.275548],
    },
    "9": {
        "NTMZONE": 9,
        "UTM": 32,
        "UTM30": [1125588.543124, 6960668.054356],
        "UTM31": [816218.407137, 6916828.164771],
        "UTM32": [504861.7046, 6901930.2139],
        "UTM33": [193474.714508, 6915927],
        "UTM34": [-115987.576219, 6958862.00692],
        "UTM35": [-421489.047315, 7030862.909672],
        "UTM36": [-720832.573768, 7132103.018588],
        "NTM": [78878.752951, 1473472.197285],
    },
    "10": {
        "NTMZONE": 10,
        "UTM": 32,
        "UTM30": [1180807.75106, 7053239.224654],
        "UTM31": [879608.095743, 7003510.698344],
        "UTM32": [575929.9885, 6982228.145],
        "UTM33": [271761.744095, 6989339],
        "UTM34": [-30927.560803, 7024860.089117],
        "UTM35": [-330111.168905, 7088876.640632],
        "UTM36": [-623629.859839, 7181510.268903],
        "NTM": [99857.1684841801, 1552855.43167415],
    },
    "11": {
        "NTMZONE": 11,
        "UTM": 32,
        "UTM30": [1323398.671266, 6761353.364844],
        "UTM31": [993983.523095, 6701047.357969],
        "UTM32": [661765.7079, 6671189.0327],
        "UTM33": [328647.700759, 6671625],
        "UTM34": [-3516.494999, 6702356.874963],
        "UTM35": [-332821.534158, 6763543.210641],
        "UTM36": [-657211.701402, 6855472.221462],
        "NTM": [122978.725141612, 1239078.01316271],
    },
    "12": {
        "NTMZONE": 12,
        "UTM": 32,
        "UTM30": [1280237.762613, 7087243.512764],
        "UTM31": [981359.801721, 7027916.777299],
        "UTM32": [679302.0376, 6996995.5806],
        "UTM33": [376079.017399, 6994408],
        "UTM34": [73660.229348, 7020148.115448],
        "UTM35": [-225953.667101, 7074276.397418],
        "UTM36": [-520655.786528, 7156901.487706],
        "NTM": [102438.076432, 1563560.196897],
    },
    "13": {
        "NTMZONE": 13,
        "UTM": 33,
        "UTM30": [1201781.30514, 7570615.357455],
        "UTM31": [949692.483138, 7514598.96232],
        "UTM32": [694069.4732, 7483397.9907],
        "UTM33": [436939.955036, 7477059],
        "UTM34": [180298.715477, 7495589.542962],
        "UTM35": [-73848.707815, 7538964.971067],
        "UTM36": [-323443.20413, 7607113.914239],
        "NTM": [101254.827252, 2048020.79059],
        "ED50": [437006.052, 7477262.358],
        "ED50-EPSGIO": [437011.88, 7477262.21],
        "3857": [1506069.46, 10271849.91],
        "4326": [13.5292522, 67.4030463],
    },
    "14": {
        "NTMZONE": 14,
        "UTM": 33,
        "UTM30": [1234741.769498, 7648085.846592],
        "UTM31": [989910.38046, 7588217.687841],
        "UTM32": [741140.6742, 7552620.3451],
        "UTM33": [490458.463193, 7541365],
        "UTM34": [239851.600154, 7554472.493731],
        "UTM35": [-8690.542671, 7591918.53549],
        "UTM36": [-253137.719875, 7653627.364659],
        "NTM": [111377.637508, 2113107.659562],
    },
    "15": {
        "NTMZONE": 15,
        "UTM": 33,
        "UTM30": [1260877.200992, 7707225.696603],
        "UTM31": [1021599.8748, 7644302.713402],
        "UTM32": [778059.2632, 7605229.3344],
        "UTM33": [532278.310163, 7590099],
        "UTM34": [286238.752207, 7598944.848781],
        "UTM35": [41917.460548, 7631747.603563],
        "UTM36": [-198676.789748, 7688431.404617],
        "NTM": [111762.40047, 2161674.939121],
    },
    "16": {
        "NTMZONE": 16,
        "UTM": 33,
        "UTM30": [1318182.850976, 7652298.815984],
        "UTM31": [1073037.661668, 7584256.943002],
        "UTM32": [823284.5347, 7540621.8036],
        "UTM33": [570974.665436, 7521479],
        "UTM34": [318107.636893, 7526861.409993],
        "UTM35": [66671.481603, 7556759.853379],
        "UTM36": [-181316.324411, 7611120.918726],
        "NTM": [107735.698758, 2092251.879855],
    },
    "17": {
        "NTMZONE": 17,
        "UTM": 33,
        "UTM30": [1329767.509695, 7727557.408875],
        "UTM31": [1091878.623487, 7657709.475822],
        "UTM32": [849127.547, 7611690.0875],
        "UTM33": [603556.220433, 7589613],
        "UTM34": [357155.215501, 7591527.820252],
        "UTM35": [111899.484487, 7617429.395207],
        "UTM36": [-130214.520664, 7667260.367869],
        "NTM": [100877.029812, 2159248.097667],
    },
    "18": {
        "NTMZONE": 18,
        "UTM": 34,
        "UTM30": [1362423.352316, 7768188.109587],
        "UTM31": [1128228.023774, 7694767.833707],
        "UTM32": [888815.0302, 7644916.8176],
        "UTM33": [646229.825902, 7618771],
        "UTM34": [402462.928297, 7616394.691442],
        "UTM35": [159483.544366, 7637792.325354],
        "UTM36": [-80724.865365, 7682913.305316],
        "NTM": [104051.325758, 2186259.155526],
        "ED50": [402517.546, 7616592.834],
        "ED50-EPSGIO": [402522.96, 7616591.86],
        "3857": [2070502.53, 10640605.26],
        "4326": [18.5996407, 68.6424229],
    },
    "19": {
        "NTMZONE": 19,
        "UTM": 34,
        "UTM30": [1381934.253828, 7822340.253929],
        "UTM31": [1152892.670872, 7746504.048444],
        "UTM32": [918349.9014, 7693833.948],
        "UTM33": [680345.988967, 7664492],
        "UTM34": [440865.490643, 7658560.389866],
        "UTM35": [201868.127089, 7676053.116133],
        "UTM36": [-34678.1768, 7716924.240139],
        "NTM": [100767.063432, 2229628.597157],
    },
    "20": {
        "NTMZONE": 20,
        "UTM": 34,
        "UTM30": [1395182.634413, 7902763.303021],
        "UTM31": [1173970.828041, 7824880.249815],
        "UTM32": [946961.8079, 7769517.0555],
        "UTM33": [716178.037932, 7736874],
        "UTM34": [483588.708746, 7727055.921646],
        "UTM35": [251135.987398, 7740094.574848],
        "UTM36": [20764.120991, 7775949.070096],
        "NTM": [102993.852028, 2298810.390598],
    },
    "21": {
        "NTMZONE": 21,
        "UTM": 34,
        "UTM30": [1416800.169883, 7955496.562499],
        "UTM31": [1200623.992291, 7874983.129409],
        "UTM32": [978342.6086, 7816588.2564],
        "UTM33": [751970.471623, 7780542],
        "UTM34": [523469.026789, 7766972.209689],
        "UTM35": [294770.154987, 7775925.134175],
        "UTM36": [67802.926226, 7807370.612264],
        "NTM": [104393.536222, 2338683.282336],
    },
    "22": {
        "NTMZONE": 22,
        "UTM": 34,
        "UTM30": [1438627.755635, 7983627.553797],
        "UTM31": [1225048.640609, 7900681.550718],
        "UTM32": [1005108.5856, 7839662.3746],
        "UTM33": [780821.951239, 7800820],
        "UTM34": [554149.20827, 7784299.772074],
        "UTM35": [327018.880954, 7790158.159444],
        "UTM36": [101353.171981, 7818375.359081],
        "NTM": [97333.469167, 2355497.851742],
    },
    "23": {
        "NTMZONE": 23,
        "UTM": 34,
        "UTM30": [1469368.201302, 8019274.223447],
        "UTM31": [1259055.611309, 7932929.160551],
        "UTM32": [1042027.1746, 7868274.281],
        "UTM33": [820298.481053, 7825588],
        "UTM34": [595830.076362, 7805037.626578],
        "UTM35": [370547.470435, 7806696.922832],
        "UTM36": [146365.332902, 7830560.343954],
        "NTM": [101952.207552, 2374868.198989],
    },
    "24": {
        "NTMZONE": 24,
        "UTM": 35,
        "UTM30": [1501225.967757, 8044727.842815],
        "UTM31": [1293154.230558, 7954958.008109],
        "UTM32": [1078022.7989, 7886733.5755],
        "UTM33": [857853.13252, 7840359],
        "UTM34": [634609.928389, 7816018.818729],
        "UTM35": [410219.681713, 7813805.319716],
        "UTM36": [186593.920117, 7833726.061998],
        "NTM": [103733.856207, 2383879.724587],
        "ED50": [410262.078, 7813999.743],
        "ED50-EPSGIO": [410267.27, 7813997.67],
        "3857": [2738432.82, 11204792.36],
        "4326": [24.5997606, 70.413918],
    },
    "25": {
        "NTMZONE": 25,
        "UTM": 35,
        "UTM30": [1527982.155537, 8067261.889688],
        "UTM31": [1321908.520682, 7974597.476508],
        "UTM32": [1108480.6348, 7903346.9406],
        "UTM33": [889724.691277, 7853837],
        "UTM34": [667608.971535, 7826270.983999],
        "UTM35": [444061.091468, 7820754.485014],
        "UTM36": [220990.332394, 7837307.69064],
        "NTM": [99977.81867, 2391910.590167],
    },
    "26": {
        "NTMZONE": 26,
        "UTM": 35,
        "UTM30": [1558031.186444, 8087630.465781],
        "UTM31": [1353706.895737, 7991755.676101],
        "UTM32": [1141707.3649, 7917191.4115],
        "UTM33": [924066.476997, 7864288],
        "UTM34": [702758.679442, 7833267.458613],
        "UTM35": [479714.971888, 7824250.449692],
        "UTM36": [256844.426398, 7837270.396228],
        "NTM": [98320.939671, 2396008.34421],
    },
    "27": {
        "NTMZONE": 27,
        "UTM": 35,
        "UTM30": [1577950.111086, 8129701.822656],
        "UTM31": [1377656.115785, 8031413.348304],
        "UTM32": [1169396.3066, 7954110.0005],
        "UTM33": [955197.198646, 7898174],
        "UTM34": [737027.780345, 7863854.157574],
        "UTM35": [516813.141596, 7851290.226376],
        "UTM36": [296454.008661, 7860531.505842],
        "NTM": [98428.632099, 2423086.506812],
    },
    "28": {
        "NTMZONE": 28,
        "UTM": 35,
        "UTM30": [1610147.437814, 8158146.513514],
        "UTM31": [1412398.501112, 8056335.464184],
        "UTM32": [1206314.8956, 7975338.1891],
        "UTM33": [993928.606016, 7915568],
        "UTM34": [777213.695121, 7877299.541722],
        "UTM35": [558098.147203, 7860692.049253],
        "UTM36": [338482.114332, 7865812.142155],
        "NTM": [103168.409753, 2431797.001966],
    },
    "29": {
        "NTMZONE": 29,
        "UTM": 35,
        "UTM30": [1671134.358979, 8124987.110537],
        "UTM31": [1469427.228024, 8017368.873835],
        "UTM32": [1258923.885, 7931035.8823],
        "UTM33": [1041708.859216, 7866409.928231],
        "UTM34": [819798.502729, 7823768.904884],
        "UTM35": [595153.972, 7803278.298],
        "UTM36": [369701.355898, 7805012.550053],
        "NTM": [101204.193214, 2373137.628899],
    },
    "30": {
        "NTMZONE": 30,
        "UTM": 36,
        "UTM30": [1715758.187369, 8120800.23809],
        "UTM31": [1513163.579, 8008730.727669],
        "UTM32": [1301380.2623, 7918114.3762],
        "UTM33": [1082523.596135, 7849390],
        "UTM34": [858635.126705, 7802848.758962],
        "UTM35": [631695.317138, 7778665.153672],
        "UTM36": [403643.980664, 7776923.887654],
        "NTM": [98676.460507, 2346748.492956],
        "ED50": [403673.433, 7777115.578],
        "ED50-EPSGIO": [403678.57, 7777112.08],
        "3857": [3391371.09, 11095170.11],
        "4326": [30.4652049, 70.0811209],
    },
    "35": {
        "NTMZONE": -1,
        "UTM": 30,
        "UTM30": [455419.547308, 6959258.68014],
        "UTM31": [149511.007034, 6977679.131735],
        "UTM32": [-154135.1091, 7024684.5223],
        "UTM33": [-453451.795073, 7100388],
        "UTM34": [-746207.705811, 7204927.293003],
        "UTM35": [-1029938.273771, 7338407.509527],
        "UTM36": [-1301885.57275, 7500809.448682],
        "ED50": [0, 0],
        "3857": [-431141.69, 9041876.62],
        "4326": [-3.8730117, 62.7609615],
    },
    "36": {
        "NTMZONE": -1,
        "UTM": 31,
        "UTM30": [737518.327523, 6599155.998099],
        "UTM31": [397559.530009, 6593058.238161],
        "UTM32": [58146.7777, 6617657.0786],
        "UTM33": [-278870.753634, 6673097],
        "UTM34": [-611507.14373, 6759683.34697],
        "UTM35": [-937536.122932, 6877835.722553],
        "UTM36": [-1254389.934693, 7028010.985085],
        "ED50": [397651.580, 6593276.938],
        "ED50-EPSGIO": [397652.29, 6593273.52],
        "3857": [132743.17, 8281251.45],
        "4326": [1.1924522, 59.4635129],
    },
    "37": {
        "NTMZONE": -1,
        "UTM": 32,
        "UTM30": [895542.075206, 6714445.543004],
        "UTM31": [565170.963905, 6693439.140009],
        "UTM32": [234433.0402, 6702569.8333],
        "UTM33": [-94801.342116, 6741884],
        "UTM34": [-420583.242231, 6811570.093084],
        "UTM35": [-740788.575403, 6911929.951394],
        "UTM36": [-1053024.55982, 7043316.042744],
        "ED50": [234514.511, 6702777.843],
        "3857": [465509.69, 8483057.17],
        "4326": [4.1817447, 60.3721234],
    },
}
