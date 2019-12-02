import pandas

data_01 = pandas.read_csv("sentimen_j.csv")
data_02 = pandas.read_csv("sentimen_p.csv")

#01-------------------------------------------------------------------------------------
jumlah_01 = len(data_01);
positif_01 = len(data_01[data_01.sentimen=="positif"]);
negatif_01 = len(data_01[data_01.sentimen=="negatif"]);
positif_persen_01 = positif_01/jumlah_01*100;
negatif_persen_01 = negatif_01/jumlah_01*100;

#ambil data pulau
jawa_01 = data_01[data_01.pulau == "Jawa"]
sumatera_01 = data_01[data_01.pulau == "Sumatera"]
sulawesi_01 = data_01[data_01.pulau == "Sulawesi"]
kalimantan_01 = data_01[data_01.pulau == "Kalimantan"]
kep_maluku_01 = data_01[data_01.pulau == "Kepulauan Maluku"]
kep_nusa_01 = data_01[data_01.pulau == "Kepulauan Nusa Tenggara"]
papua_01 = data_01[data_01.pulau == "Papua"]

#ambil jumlah data sentimen tiap pulau (jumlah)
jawa_pos_01 = len(jawa_01[jawa_01.sentimen=="positif"])
jawa_neg_01 = len(jawa_01[jawa_01.sentimen=="negatif"])
sumatera_pos_01 = len(sumatera_01[sumatera_01.sentimen=="positif"])
sumatera_neg_01 = len(sumatera_01[sumatera_01.sentimen=="negatif"])
sulawesi_pos_01 = len(sulawesi_01[sulawesi_01.sentimen=="positif"])
sulawesi_neg_01 = len(sulawesi_01[sulawesi_01.sentimen=="negatif"])
kalimantan_pos_01 = len(kalimantan_01[kalimantan_01.sentimen=="positif"])
kalimantan_neg_01 = len(kalimantan_01[kalimantan_01.sentimen=="negatif"])
kep_maluku_pos_01 = len(kep_maluku_01[kep_maluku_01.sentimen=="positif"])
kep_maluku_neg_01 = len(kep_maluku_01[kep_maluku_01.sentimen=="negatif"])
kep_nusa_pos_01 = len(kep_nusa_01[kep_nusa_01.sentimen=="positif"])
kep_nusa_neg_01 = len(kep_nusa_01[kep_nusa_01.sentimen=="negatif"])
papua_pos_01 = len(papua_01[papua_01.sentimen=="positif"])
papua_neg_01 = len(papua_01[papua_01.sentimen=="negatif"])

#ambil jumlah data sentimen tiap pulau (persen)
jawa_pos_persen_01 = jawa_pos_01/len(jawa_01)*100
jawa_neg_persen_01 = jawa_neg_01/len(jawa_01)*100
sumatera_pos_persen_01 = sumatera_pos_01/len(sumatera_01)*100
sumatera_neg_persen_01 = sumatera_neg_01/len(sumatera_01)*100
sulawesi_pos_persen_01 = sulawesi_pos_01/len(sulawesi_01)*100
sulawesi_neg_persen_01 = sulawesi_neg_01/len(sulawesi_01)*100
kalimantan_pos_persen_01 = kalimantan_pos_01/len(kalimantan_01)*100
kalimantan_neg_persen_01 = kalimantan_neg_01/len(kalimantan_01)*100
kep_maluku_pos_persen_01 = kep_maluku_pos_01/len(kep_maluku_01)*100
kep_maluku_neg_persen_01 = kep_maluku_neg_01/len(kep_maluku_01)*100
kep_nusa_pos_persen_01 = kep_nusa_pos_01/len(kep_nusa_01)*100
kep_nusa_neg_persen_01 = kep_nusa_neg_01/len(kep_nusa_01)*100
papua_pos_persen_01 = papua_pos_01/len(papua_01)*100
papua_neg_persen_01 = papua_neg_01/len(papua_01)*100

#debat-pasca
debat1_01 = data_01[(data_01.waktu=="debat 1")]
debat2_01 = data_01[(data_01.waktu=="debat 2")]
debat3_01 = data_01[(data_01.waktu=="debat 3")]
debat4_01 = data_01[(data_01.waktu=="debat 4")]
debat5_01 = data_01[(data_01.waktu=="debat 5")]
debat1_pos_01 = len(debat1_01[debat1_01.sentimen=="positif"])/len(debat1_01)*100
debat2_pos_01 = len(debat2_01[debat2_01.sentimen=="positif"])/len(debat2_01)*100
debat3_pos_01 = len(debat3_01[debat3_01.sentimen=="positif"])/len(debat3_01)*100
debat4_pos_01 = len(debat4_01[debat4_01.sentimen=="positif"])/len(debat4_01)*100
debat5_pos_01 = len(debat5_01[debat5_01.sentimen=="positif"])/len(debat5_01)*100
debat1_neg_01 = len(debat1_01[debat1_01.sentimen=="negatif"])/len(debat1_01)*100
debat2_neg_01 = len(debat2_01[debat2_01.sentimen=="negatif"])/len(debat2_01)*100
debat3_neg_01 = len(debat3_01[debat3_01.sentimen=="negatif"])/len(debat3_01)*100
debat4_neg_01 = len(debat4_01[debat4_01.sentimen=="negatif"])/len(debat4_01)*100
debat5_neg_01 = len(debat5_01[debat5_01.sentimen=="negatif"])/len(debat5_01)*100

#Sebelum sesudah
indo_pre_01 = data_01[(data_01.pemilu=="pre")]
indo_pasca_01 = data_01[(data_01.pemilu=="pasca")]
jawa_pre_01 = jawa_01[(jawa_01.pemilu=="pre")]
sumatera_pre_01 = sumatera_01[(sumatera_01.pemilu=="pre")]
sulawesi_pre_01 = sulawesi_01[(sulawesi_01.pemilu=="pre")]
kalimantan_pre_01 = kalimantan_01[(kalimantan_01.pemilu=="pre")]
kep_maluku_pre_01 = kep_maluku_01[(kep_maluku_01.pemilu=="pre")]
kep_nusa_pre_01 = kep_nusa_01[(kep_nusa_01.pemilu=="pre")]
papua_pre_01 = papua_01[(papua_01.pemilu=="pre")]
jawa_pasca_01 = jawa_01[(jawa_01.pemilu=="pasca")]
sumatera_pasca_01 = sumatera_01[(sumatera_01.pemilu=="pasca")]
sulawesi_pasca_01 = sulawesi_01[(sulawesi_01.pemilu=="pasca")]
kalimantan_pasca_01 = kalimantan_01[(kalimantan_01.pemilu=="pasca")]
kep_maluku_pasca_01 = kep_maluku_01[(kep_maluku_01.pemilu=="pasca")]
kep_nusa_pasca_01 = kep_nusa_01[(kep_nusa_01.pemilu=="pasca")]
papua_pasca_01 = papua_01[(papua_01.pemilu=="pasca")]

indo_pre_pos_01 = len(indo_pre_01[indo_pre_01.sentimen=="positif"])/len(indo_pre_01)*100
jawa_pre_pos_01 = len(jawa_pre_01[jawa_pre_01.sentimen=="positif"])/len(jawa_pre_01)*100
sumatera_pre_pos_01 = len(sumatera_pre_01[sumatera_pre_01.sentimen=="positif"])/len(sumatera_pre_01)*100
sulawesi_pre_pos_01 = len(sulawesi_pre_01[sulawesi_pre_01.sentimen=="positif"])/len(sulawesi_pre_01)*100
kalimantan_pre_pos_01 = len(kalimantan_pre_01[kalimantan_pre_01.sentimen=="positif"])/len(kalimantan_pre_01)*100
kep_maluku_pre_pos_01 = len(kep_maluku_pre_01[kep_maluku_pre_01.sentimen=="positif"])/len(kep_maluku_pre_01)*100
kep_nusa_pre_pos_01 = len(kep_nusa_pre_01[kep_nusa_pre_01.sentimen=="positif"])/len(kep_nusa_pre_01)*100
papua_pre_pos_01 = len(papua_pre_01[papua_pre_01.sentimen=="positif"])/len(papua_pre_01)*100
indo_pasca_pos_01 = len(indo_pasca_01[indo_pasca_01.sentimen=="positif"])/len(indo_pasca_01)*100
jawa_pasca_pos_01 = len(jawa_pasca_01[jawa_pasca_01.sentimen=="positif"])/len(jawa_pasca_01)*100
sumatera_pasca_pos_01 = len(sumatera_pasca_01[sumatera_pasca_01.sentimen=="positif"])/len(sumatera_pasca_01)*100
sulawesi_pasca_pos_01 = len(sulawesi_pasca_01[sulawesi_pasca_01.sentimen=="positif"])/len(sulawesi_pasca_01)*100
kalimantan_pasca_pos_01 = len(kalimantan_pasca_01[kalimantan_pasca_01.sentimen=="positif"])/len(kalimantan_pasca_01)*100
kep_maluku_pasca_pos_01 = len(kep_maluku_pasca_01[kep_maluku_pasca_01.sentimen=="positif"])/len(kep_maluku_pasca_01)*100
kep_nusa_pasca_pos_01 = len(kep_nusa_pasca_01[kep_nusa_pasca_01.sentimen=="positif"])/len(kep_nusa_pasca_01)*100
papua_pasca_pos_01 = len(papua_pasca_01[papua_pasca_01.sentimen=="positif"])/len(papua_pasca_01)*100

indo_pre_neg_01 = len(indo_pre_01[indo_pre_01.sentimen=="negatif"])/len(indo_pre_01)*100
jawa_pre_neg_01 = len(jawa_pre_01[jawa_pre_01.sentimen=="negatif"])/len(jawa_pre_01)*100
sumatera_pre_neg_01 = len(sumatera_pre_01[sumatera_pre_01.sentimen=="negatif"])/len(sumatera_pre_01)*100
sulawesi_pre_neg_01 = len(sulawesi_pre_01[sulawesi_pre_01.sentimen=="negatif"])/len(sulawesi_pre_01)*100
kalimantan_pre_neg_01 = len(kalimantan_pre_01[kalimantan_pre_01.sentimen=="negatif"])/len(kalimantan_pre_01)*100
kep_maluku_pre_neg_01 = len(kep_maluku_pre_01[kep_maluku_pre_01.sentimen=="negatif"])/len(kep_maluku_pre_01)*100
kep_nusa_pre_neg_01 = len(kep_nusa_pre_01[kep_nusa_pre_01.sentimen=="negatif"])/len(kep_nusa_pre_01)*100
papua_pre_neg_01 = len(papua_pre_01[papua_pre_01.sentimen=="negatif"])/len(papua_pre_01)*100
indo_pasca_neg_01 = len(indo_pasca_01[indo_pasca_01.sentimen=="negatif"])/len(indo_pasca_01)*100
jawa_pasca_neg_01 = len(jawa_pasca_01[jawa_pasca_01.sentimen=="negatif"])/len(jawa_pasca_01)*100
sumatera_pasca_neg_01 = len(sumatera_pasca_01[sumatera_pasca_01.sentimen=="negatif"])/len(sumatera_pasca_01)*100
sulawesi_pasca_neg_01 = len(sulawesi_pasca_01[sulawesi_pasca_01.sentimen=="negatif"])/len(sulawesi_pasca_01)*100
kalimantan_pasca_neg_01 = len(kalimantan_pasca_01[kalimantan_pasca_01.sentimen=="negatif"])/len(kalimantan_pasca_01)*100
kep_maluku_pasca_neg_01 = len(kep_maluku_pasca_01[kep_maluku_pasca_01.sentimen=="negatif"])/len(kep_maluku_pasca_01)*100
kep_nusa_pasca_neg_01 = len(kep_nusa_pasca_01[kep_nusa_pasca_01.sentimen=="negatif"])/len(kep_nusa_pasca_01)*100
papua_pasca_neg_01 = len(papua_pasca_01[papua_pasca_01.sentimen=="negatif"])/len(papua_pasca_01)*100

#02--------------------------------------------------------------------------
jumlah_02 = len(data_02);
positif_02 = len(data_02[data_02.sentimen=="positif"]);
negatif_02 = len(data_02[data_02.sentimen=="negatif"]);
positif_persen_02 = positif_02/jumlah_02*100;
negatif_persen_02 = negatif_02/jumlah_02*100;

#island
jawa_02 = data_02[data_02.pulau == "Jawa"]
sumatera_02 = data_02[data_02.pulau == "Sumatera"]
sulawesi_02 = data_02[data_02.pulau == "Sulawesi"]
kalimantan_02 = data_02[data_02.pulau == "Kalimantan"]
kep_maluku_02 = data_02[data_02.pulau == "Kepulauan Maluku"]
kep_nusa_02 = data_02[data_02.pulau == "Kepulauan Nusa Tenggara"]
papua_02 = data_02[data_02.pulau == "Papua"]

#data based on time
debat1_02 = data_02[(data_02.waktu=="debat 1")]
debat2_02 = data_02[(data_02.waktu=="debat 2")]
debat3_02 = data_02[(data_02.waktu=="debat 3")]
debat4_02 = data_02[(data_02.waktu=="debat 4")]
debat5_02 = data_02[(data_02.waktu=="debat 5")]
debat1_pos_02 = len(debat1_02[debat1_02.sentimen=="positif"])/len(debat1_02)*100
debat2_pos_02 = len(debat2_02[debat2_02.sentimen=="positif"])/len(debat2_02)*100
debat3_pos_02 = len(debat3_02[debat3_02.sentimen=="positif"])/len(debat3_02)*100
debat4_pos_02 = len(debat4_02[debat4_02.sentimen=="positif"])/len(debat4_02)*100
debat5_pos_02 = len(debat5_02[debat5_02.sentimen=="positif"])/len(debat5_02)*100
debat1_neg_02 = len(debat1_02[debat1_02.sentimen=="negatif"])/len(debat1_02)*100
debat2_neg_02 = len(debat2_02[debat2_02.sentimen=="negatif"])/len(debat2_02)*100
debat3_neg_02 = len(debat3_02[debat3_02.sentimen=="negatif"])/len(debat3_02)*100
debat4_neg_02 = len(debat4_02[debat4_02.sentimen=="negatif"])/len(debat4_02)*100
debat5_neg_02 = len(debat5_02[debat5_02.sentimen=="negatif"])/len(debat5_02)*100

#ambil jumlah data sentimen tiap pulau (jumlah)
jawa_pos_02 = len(jawa_02[jawa_02.sentimen=="positif"])
jawa_neg_02 = len(jawa_02[jawa_02.sentimen=="negatif"])
sumatera_pos_02 = len(sumatera_02[sumatera_02.sentimen=="positif"])
sumatera_neg_02 = len(sumatera_02[sumatera_02.sentimen=="negatif"])
sulawesi_pos_02 = len(sulawesi_02[sulawesi_02.sentimen=="positif"])
sulawesi_neg_02 = len(sulawesi_02[sulawesi_02.sentimen=="negatif"])
kalimantan_pos_02 = len(kalimantan_02[kalimantan_02.sentimen=="positif"])
kalimantan_neg_02 = len(kalimantan_02[kalimantan_02.sentimen=="negatif"])
kep_maluku_pos_02 = len(kep_maluku_02[kep_maluku_02.sentimen=="positif"])
kep_maluku_neg_02 = len(kep_maluku_02[kep_maluku_02.sentimen=="negatif"])
kep_nusa_pos_02 = len(kep_nusa_02[kep_nusa_02.sentimen=="positif"])
kep_nusa_neg_02 = len(kep_nusa_02[kep_nusa_02.sentimen=="negatif"])
papua_pos_02 = len(papua_02[papua_02.sentimen=="positif"])
papua_neg_02 = len(papua_02[papua_02.sentimen=="negatif"])

#ambil jumlah data sentimen tiap pulau (persen)
jawa_pos_persen_02 = jawa_pos_02/len(jawa_02)*100
jawa_neg_persen_02 = jawa_neg_02/len(jawa_02)*100
sumatera_pos_persen_02 = sumatera_pos_02/len(sumatera_02)*100
sumatera_neg_persen_02 = sumatera_neg_02/len(sumatera_02)*100
sulawesi_pos_persen_02 = sulawesi_pos_02/len(sulawesi_02)*100
sulawesi_neg_persen_02 = sulawesi_neg_02/len(sulawesi_02)*100
kalimantan_pos_persen_02 = kalimantan_pos_02/len(kalimantan_02)*100
kalimantan_neg_persen_02 = kalimantan_neg_02/len(kalimantan_02)*100
kep_maluku_pos_persen_02 = kep_maluku_pos_02/len(kep_maluku_02)*100
kep_maluku_neg_persen_02 = kep_maluku_neg_02/len(kep_maluku_02)*100
kep_nusa_pos_persen_02 = kep_nusa_pos_02/len(kep_nusa_02)*100
kep_nusa_neg_persen_02 = kep_nusa_neg_02/len(kep_nusa_02)*100
papua_pos_persen_02 = papua_pos_02/len(papua_02)*100
papua_neg_persen_02 = papua_neg_02/len(papua_02)*100

indo_pre_02 = data_02[(data_02.pemilu=="pre")]
indo_pasca_02 = data_02[(data_02.pemilu=="pasca")]
jawa_pre_02 = jawa_02[(jawa_02.pemilu=="pre")]
sumatera_pre_02 = sumatera_02[(sumatera_02.pemilu=="pre")]
sulawesi_pre_02 = sulawesi_02[(sulawesi_02.pemilu=="pre")]
kalimantan_pre_02 = kalimantan_02[(kalimantan_02.pemilu=="pre")]
kep_maluku_pre_02 = kep_maluku_02[(kep_maluku_02.pemilu=="pre")]
kep_nusa_pre_02 = kep_nusa_02[(kep_nusa_02.pemilu=="pre")]
papua_pre_02 = papua_02[(papua_02.pemilu=="pre")]
jawa_pasca_02 = jawa_02[(jawa_02.pemilu=="pasca")]
sumatera_pasca_02 = sumatera_02[(sumatera_02.pemilu=="pasca")]
sulawesi_pasca_02 = sulawesi_02[(sulawesi_02.pemilu=="pasca")]
kalimantan_pasca_02 = kalimantan_02[(kalimantan_02.pemilu=="pasca")]
kep_maluku_pasca_02 = kep_maluku_02[(kep_maluku_02.pemilu=="pasca")]
kep_nusa_pasca_02 = kep_nusa_02[(kep_nusa_02.pemilu=="pasca")]
papua_pasca_02 = papua_02[(papua_02.pemilu=="pasca")]

indo_pre_pos_02 = len(indo_pre_02[indo_pre_02.sentimen=="positif"])/len(indo_pre_02)*100
jawa_pre_pos_02 = len(jawa_pre_02[jawa_pre_02.sentimen=="positif"])/len(jawa_pre_02)*100
sumatera_pre_pos_02 = len(sumatera_pre_02[sumatera_pre_02.sentimen=="positif"])/len(sumatera_pre_02)*100
sulawesi_pre_pos_02 = len(sulawesi_pre_02[sulawesi_pre_02.sentimen=="positif"])/len(sulawesi_pre_02)*100
kalimantan_pre_pos_02 = len(kalimantan_pre_02[kalimantan_pre_02.sentimen=="positif"])/len(kalimantan_pre_02)*100
kep_maluku_pre_pos_02 = len(kep_maluku_pre_02[kep_maluku_pre_02.sentimen=="positif"])/len(kep_maluku_pre_02)*100
kep_nusa_pre_pos_02 = len(kep_nusa_pre_02[kep_nusa_pre_02.sentimen=="positif"])/len(kep_nusa_pre_02)*100
papua_pre_pos_02 = len(papua_pre_02[papua_pre_02.sentimen=="positif"])/len(papua_pre_02)*100
indo_pasca_pos_02 = len(indo_pasca_02[indo_pasca_02.sentimen=="positif"])/len(indo_pasca_02)*100
jawa_pasca_pos_02 = len(jawa_pasca_02[jawa_pasca_02.sentimen=="positif"])/len(jawa_pasca_02)*100
sumatera_pasca_pos_02 = len(sumatera_pasca_02[sumatera_pasca_02.sentimen=="positif"])/len(sumatera_pasca_02)*100
sulawesi_pasca_pos_02 = len(sulawesi_pasca_02[sulawesi_pasca_02.sentimen=="positif"])/len(sulawesi_pasca_02)*100
kalimantan_pasca_pos_02 = len(kalimantan_pasca_02[kalimantan_pasca_02.sentimen=="positif"])/len(kalimantan_pasca_02)*100
kep_maluku_pasca_pos_02 = len(kep_maluku_pasca_02[kep_maluku_pasca_02.sentimen=="positif"])/len(kep_maluku_pasca_02)*100
kep_nusa_pasca_pos_02 = len(kep_nusa_pasca_02[kep_nusa_pasca_02.sentimen=="positif"])/len(kep_nusa_pasca_02)*100
papua_pasca_pos_02 = len(papua_pasca_02[papua_pasca_02.sentimen=="positif"])/len(papua_pasca_02)*100

indo_pre_neg_02 = len(indo_pre_02[indo_pre_02.sentimen=="negatif"])/len(indo_pre_02)*100
jawa_pre_neg_02 = len(jawa_pre_02[jawa_pre_02.sentimen=="negatif"])/len(jawa_pre_02)*100
sumatera_pre_neg_02 = len(sumatera_pre_02[sumatera_pre_02.sentimen=="negatif"])/len(sumatera_pre_02)*100
sulawesi_pre_neg_02 = len(sulawesi_pre_02[sulawesi_pre_02.sentimen=="negatif"])/len(sulawesi_pre_02)*100
kalimantan_pre_neg_02 = len(kalimantan_pre_02[kalimantan_pre_02.sentimen=="negatif"])/len(kalimantan_pre_02)*100
kep_maluku_pre_neg_02 = len(kep_maluku_pre_02[kep_maluku_pre_02.sentimen=="negatif"])/len(kep_maluku_pre_02)*100
kep_nusa_pre_neg_02 = len(kep_nusa_pre_02[kep_nusa_pre_02.sentimen=="negatif"])/len(kep_nusa_pre_02)*100
papua_pre_neg_02 = len(papua_pre_02[papua_pre_02.sentimen=="negatif"])/len(papua_pre_02)*100
indo_pasca_neg_02 = len(indo_pasca_02[indo_pasca_02.sentimen=="negatif"])/len(indo_pasca_02)*100
jawa_pasca_neg_02 = len(jawa_pasca_02[jawa_pasca_02.sentimen=="negatif"])/len(jawa_pasca_02)*100
sumatera_pasca_neg_02 = len(sumatera_pasca_02[sumatera_pasca_02.sentimen=="negatif"])/len(sumatera_pasca_02)*100
sulawesi_pasca_neg_02 = len(sulawesi_pasca_02[sulawesi_pasca_02.sentimen=="negatif"])/len(sulawesi_pasca_02)*100
kalimantan_pasca_neg_02 = len(kalimantan_pasca_02[kalimantan_pasca_02.sentimen=="negatif"])/len(kalimantan_pasca_02)*100
kep_maluku_pasca_neg_02 = len(kep_maluku_pasca_02[kep_maluku_pasca_02.sentimen=="negatif"])/len(kep_maluku_pasca_02)*100
kep_nusa_pasca_neg_02 = len(kep_nusa_pasca_02[kep_nusa_pasca_02.sentimen=="negatif"])/len(kep_nusa_pasca_02)*100
papua_pasca_neg_02 = len(papua_pasca_02[papua_pasca_02.sentimen=="negatif"])/len(papua_pasca_02)*100

#----------------------------------------------------------------------
#jumlah keseluruhan untuk card
jumlah = jumlah_01+jumlah_02;
positif = positif_01+positif_02;
negatif = negatif_01+negatif_02;

#perhitungan fluktuatif untuk grafik pertama
jumlah_jawa_01 = jawa_pos_01-jawa_neg_01;
jumlah_jawa_02 = jawa_pos_02-jawa_neg_02;
jumlah_sumatera_01 = sumatera_pos_01-sumatera_neg_01;
jumlah_sumatera_02 = sumatera_pos_02-sumatera_neg_02;
jumlah_sulawesi_01 = sulawesi_pos_01-sulawesi_neg_01;
jumlah_sulawesi_02 = sulawesi_pos_02-sulawesi_neg_02;
jumlah_kalimantan_01 = kalimantan_pos_01-kalimantan_neg_01;
jumlah_kalimantan_02 = kalimantan_pos_02-kalimantan_neg_02;
jumlah_kep_maluku_01 = kep_maluku_pos_01-kep_maluku_neg_01;
jumlah_kep_maluku_02 = kep_maluku_pos_02-kep_maluku_neg_02;
jumlah_kep_nusa_01 = kep_nusa_pos_01-kep_nusa_neg_01;
jumlah_kep_nusa_02 = kep_nusa_pos_02-kep_nusa_neg_02;
jumlah_papua_01 = papua_pos_01-papua_neg_01;
jumlah_papua_02 = papua_pos_02-papua_neg_02;

# time = pd.read_csv("sentimen_02.csv", index_col="waktu")
