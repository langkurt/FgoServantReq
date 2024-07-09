import pandas as pd
from bs4 import BeautifulSoup

# Replace 'servants.html' with the path to your HTML file
file_path = 'html/servants1.html'

# Read the HTML content from the file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
rows = soup.find_all('tr')

# Extract the data from the table
data = []
for row in rows:
    columns = row.find_all('td')
    if not columns:
        continue
    index = columns[0].text.strip()
    servant_name = columns[2].text.strip()
    data.append([index, servant_name])

# Create a DataFrame from the extracted data
df = pd.DataFrame(data, columns=['Servant ID', 'Servant Name'])

# Display the DataFrame
# print(df.to_string(index=False))


data_mapping = {int(row['Servant ID']): row['Servant Name'] for _, row in df.iterrows()}
print(data_mapping)

"""
Servant ID                      Servant Name
         1                  Mashu Kyrielight
         2                 Artoria Pendragon
         3         Artoria Pendragon (Alter)
         4          Artoria Pendragon (Lily)
         5                     Nero Claudius
         6                         Siegfried
         7               Gaius Julius Caesar
         8                            Altera
         9                    Gilles de Rais
        10                   Chevalier d'Eon
        11                             EMIYA
        12                         Gilgamesh
        13                        Robin Hood
        14                          Atalanta
        15                           Euryale
        16                             Arash
        17                       Cú Chulainn
        18                 Elizabeth Báthory
        19                  Musashibō Benkei
        20           Cú Chulainn (Prototype)
        21                        Leonidas I
        22                           Romulus
        23                            Medusa
        24                          Georgios
        25                      Edward Teach
        26                           Boudica
        27                      Ushiwakamaru
        28                         Alexander
        29                  Marie Antoinette
        30                            Martha
        31                             Medea
        32                    Gilles de Rais
        33           Hans Christian Andersen
        34               William Shakespeare
        35                    Mephistopheles
        36           Wolfgang Amadeus Mozart
        37   Zhuge Liang (Lord El-Melloi II)
        38                       Cú Chulainn
        39                     Sasaki Kojirō
        40          Hassan of the Cursed Arm
        41                            Stheno
        42                           Jing Ke
        43              Charles-Henri Sanson
        44              Phantom of the Opera
        45                         Mata Hari
        46                          Carmilla
        47                          Heracles
        48                          Lancelot
        49                    Lu Bu Fengxian
        50                         Spartacus
        51                    Sakata Kintoki
        52                          Vlad III
        53                          Asterios
        54                          Caligula
        55                        Darius III
        56                          Kiyohime
        57                     Eric Bloodaxe
        58                        Tamamo Cat
        59                      Jeanne d'Arc
        60                             Orion
        61     Elizabeth Báthory (Halloween)
        62                     Tamamo no Mae
        63                             David
        64                            Hector
        65                     Francis Drake
        66            Anne Bonny & Mary Read
        67                      Medea (Lily)
        68                        Okita Sōji
        69                      Oda Nobunaga
        70                          Scáthach
        71               Diarmuid Ua Duibhne
        72                  Fergus mac Róich
        73   Artoria Pendragon (Santa Alter)
        74                     Nursery Rhyme
        75                   Jack the Ripper
        76                           Mordred
        77                      Nikola Tesla
        78         Artoria Pendragon (Alter)
        79          Paracelsus von Hohenheim
        80                   Charles Babbage
        81               Henry Jekyll & Hyde
        82                      Frankenstein
        83                           Solomon
        84                            Arjuna
        85                             Karna
        86              Mysterious Heroine X
        87                Fionn mac Cumhaill
        88                         Brynhildr
        89                           Beowulf
        90             Nero Claudius (Bride)
        91                       Ryōgi Shiki
        92                       Ryōgi Shiki
        93                     Amakusa Shirō
        94                           Astolfo
        95                           Kid Gil
        96                     Edmond Dantès
        97                       Nightingale
        98               Cú Chulainn (Alter)
        99                        Queen Medb
       100                  Helena Blavatsky
       101                              Rama
       102                         Li Shuwen
       103                     Thomas Edison
       104                          Geronimo
       105                     Billy the Kid
       106              Jeanne d'Arc (Alter)
       107                      Angra Mainyu
       108                          Iskandar
       109                  EMIYA (Assassin)
       110       Hassan of the Hundred Faces
       111        Irisviel (Dress of Heaven)
       112                       Shuten Dōji
       113                  Xuanzang Sanzang
       114                 Minamoto no Raikō
       115                    Sakata Kintoki
       116                      Ibaraki Dōji
       117                       Fūma Kotarō
       118                        Ozymandias
       119                 Artoria Pendragon
       120                          Nitocris
       121                          Lancelot
       122                           Tristan
       123                            Gawain
       124            Hassan of the Serenity
       125                       Tawara Tōta
       126                          Bedivere
       127                 Leonardo Da Vinci
       128                     Tamamo no Mae
       129                 Artoria Pendragon
       130                  Marie Antoinette
       131            Anne Bonny & Mary Read
       132                           Mordred
       133                          Scáthach
       134                          Kiyohime
       135                            Martha
       136           Illyasviel von Einzbern
       137                Chloe von Einzbern
       138         Elizabeth Báthory (Brave)
       139                         Cleopatra
       140                  Vlad III (EXTRA)
       141     Jeanne d'Arc Alter Santa Lily
       142                            Ishtar
       143                            Enkidu
       144                      Quetzalcoatl
       145                         Gilgamesh
       146                            Medusa
       147                            Gorgon
       148                        Jaguar Man
       149                            Tiamat
       150                            Merlin
       151                            Goetia
       152                           Solomon
       153                  Miyamoto Musashi
       154     "The Old Man of the Mountain"
       155      Mysterious Heroine X (Alter)
       156                    James Moriarty
       157                     EMIYA (Alter)
       158                      Hessian Lobo
       159                          Yan Qing
       160      Arthur Pendragon (Prototype)
       161                  Hijikata Toshizō
       162                            Chacha
       163                        Meltryllis
       164                        Passionlip
       165                      Suzuka Gozen
       166                                BB
       167                    Sesshōin Kiara
       168                       Beast III/R
       169                      Scheherazade
       170                         Wu Zetian
       171                       Penthesilea
       172              Christopher Columbus
       173                   Sherlock Holmes
       174                       Paul Bunyan
       175                     Nero Claudius
       176                      Frankenstein
       177                          Nitocris
       178                      Oda Nobunaga
       179         Artoria Pendragon (Alter)
       180                  Helena Blavatsky
       181                 Minamoto no Raikō
       182                            Ishtar
       183                           Parvati
       184                       Tomoe Gozen
       185                 Mochizuki Chiyome
       186                     Hōzōin Inshun
       187     Yagyū Tajima no Kami Munenori
       188                        Katō Danzō
       189                       Osakabehime
       190                    Mecha Eli-chan
       191              Mecha Eli-chan Mk.II
       192                             Circe
       193                             Nezha
       194                    Queen of Sheba
       195                  Abigail Williams
       196                        Ereshkigal
       197                Altera the San(ta)
       198                Katsushika Hokusai
       199                         Semiramis
       200                    Asagami Fujino
       201                         Anastasia
       202                  Atalanta (Alter)
       203                         Avicebron
       204                   Antonio Salieri
       205                 Ivan the Terrible
       206                          Achilles
       207                            Chiron
       208                              Sieg
       209                Okita Sōji (Alter)
       210                         Okada Izō
       211                    Sakamoto Ryōma
       212                          Napoléon
       213                            Sigurd
       214                          Valkyrie
       215                    Scáthach-Skaði
       216                      Jeanne d'Arc
       217                      Ibaraki Dōji
       218                      Ushiwakamaru
       219              Jeanne d'Arc (Alter)
       220                                BB
       221                        Queen Medb
       222             Mysterious Heroine XX
       223               Diarmuid Ua Duibhne
       224                           Sitonai
       225                       Shuten Dōji
       226                          Xiang Yu
       227                      Lanling Wang
       228                       Qin Liangyu
       229                      Shi Huang Di
       230                        Consort Yu
       231                          Red Hare
       232                        Bradamante
       233        Quetzalcoatl (Samba/Santa)
       234                         Beni-Enma
       235                         Li Shuwen
       236                     Miyu Edelfelt
       237                  Murasaki Shikibu
       238                        Kingprotea
       239                              Kama
       240                       Beast III/L
       241                  Sima Yi (Reines)
       242                           Astraea
       243                              Gray
       244                   Jinako Carigiri
       245                        Lakshmibai
       246                      William Tell
       247                    Arjuna (Alter)
       248                       Aśvatthāman
       249                         Asclepius
       250               Demon King Nobunaga
       251                    Mori Nagayoshi
       252                    Nagao Kagetora
       253                 Leonardo Da Vinci
       254                             Jason
       255                             Paris
       256                            Gareth
       257               Bartholomew Roberts
       258                         Chen Gong
       259                  Charlotte Corday
       260                            Salome
       261                  Miyamoto Musashi
       262                       Osakabehime
       263                          Carmilla
       264                Katsushika Hokusai
       265                 Artoria Pendragon
       266            Mysterious Alter Ego Λ
       267                      Okita J Sōji
       268                      Space Ishtar
       269                     Calamity Jane
       270                           Astolfo
       271               Nightingale (Santa)
       272                       Super Orion
       273                       Mandricardo
       274                            Europa
       275                       Yang Guifei
       276                      Sei Shōnagon
       277                          Odysseus
       278                          Dioscuri
       279                            Caenis
       280                  Romulus-Quirinus
       281                           Voyager
       282                        Kijyo Kōyō
       283                      Utsumi Erice
       284                    Artoria Caster
       285                    Sesshōin Kiara
       286           Illyasviel von Einzbern
       287                         Brynhildr
       288                        Consort Yu
       289         Abigail Williams (Summer)
       290                       Tomoe Gozen
       291                  Murasaki Shikibu
       292                            Himiko
       293                      Saitō Hajime
       294                     Oda Nobukatsu
       295                          Van Gogh
       296                              Nemo
       297                      Ashiya Dōman
       298                 Watanabe no Tsuna
       299                        Ibuki Dōji
       300                            Vritra
       301                     Karna (Santa)
       302                    Senji Muramasa
       303                 Taira no Kagekiyo
       304                      Kiichi Hōgen
       305                      Amor (Caren)
       306                           Galatea
       307                        Miss Crane
       308         Mysterious Idol X (Alter)
       309                            Morgan
       310                          Barghest
       311                      Baobhan Sith
       312                          Mélusine
       313                          Percival
       314               Koyanskaya of Light
       315                          Habetrot
       316                            Oberon
       317                Okita Sōji (Alter)
       318                   Anastasia & Viy
       319                  Charlotte Corday
       320                 Leonardo Da Vinci
       321                              Kama
       322                            Caenis
       323                      Sei Shōnagon
       324                  Jacques de Molay
       325                           Zenobia
       326    Elizabeth Báthory (Cinderella)
       327                    Izumo no Okuni
       328              Mysterious Ranmaru X
       329                    Sakamoto Ryōma
       330                    Martha (Santa)
       331                      Taigong Wang
       332                 Dobrynya Nikitich
       333                          Beast IV
       334            Koyanskaya of Darkness
       335                       Hephaestion
       336         Manannán mac Lir (Bazett)
       337                     Trung Sisters
       338                    Taisui Xingjun
       339                      Super Bunyan
       340                        Daikokuten
       341                       Mary Anning
       342                    Constantine XI
       343                       Charlemagne
       344                            Roland
       345                         Kriemhild
       346                    James Moriarty
       347                       Don Quixote
       348                         Zhang Jue
       349                    Kyokutei Bakin
       350              Minamoto no Tametomo
       351                  Archetype: Earth
       352                             Xu Fu
       353                       Lady Avalon
       354                            Gareth
       355                        Ibuki Dōji
       356                      Utsumi Erice
       357                    Scáthach-Skaði
       358                         Wu Zetian
       359                             Thrúd
       360                             Hildr
       361                          Ortlinde
       362                      Sen no Rikyū
       363                  Yamanami Keisuke
       364                               Iyo
       365                        Huyan Zhuo
       366                       Huang Feihu
       367          Nine-Tattoo Dragon Eliza
       368                         Britomart
       369                  Grigori Rasputin
       370                  Nitocris (Alter)
       371                      Tezcatlipoca
       372                      Tenochtitlan
       373                          Kukulkan
       374                    Popess Johanna
       375                 Takasugi Shinsaku
       376                      Larva/Tiamat
       377               Sodom's Beast/Draco
       378                           Locusta
       379                           Sétanta
       380                       Kashin Koji
       381                             Bhima
       382                        Duryodhana
       383                             Durga
       384                            Medusa
       385                   Aesc the Savior
       386                    Artoria Caster
       387    Suzuka Gozen (Summer Vacation)
       388                Chloe von Einzbern
       389          Cnoc na Riabh Yaraan-doo
       390                          Mélusine
       391                      UDK-Barghest
       392              Cait Cú Cerpriestess
       393                          Wandjina
       394                        Ptolemaios
       395                  Sugitani Zenjūbō
       396                           Theseus
       397                    Takeda Shingen
       398                Nagakura Shinpachi
       399                    Saika Magoichi
       400                    Uesugi Kenshin
       401                      Nemo (Santa)
       402                     Yamato Takeru
       403      Minamoto no Raikō/Ushi Gozen
       404                      Yui Shōsetsu
       405                     Miyamoto Iori
       406                         Andromeda
       407          Marie Antoinette (Alter)
       408        Hassan of the Shining Star
       409  King of the Cavern, Monte Cristo
       410          Alessandro di Cagliostro
       411                     E-Flare Marie
       412                      E-Aqua Marie
       413                       Aozaki Aoko
       414                    Shizuki Sōjūrō
       415                      Kuonji Alice
       416 Azumi no Isora (Hibiki & Chikagi)


"""