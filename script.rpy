label splashscreen:
    scene black
    pause 1.0
    show text "WOTABO 1st Project" with dissolve
    pause 1.0
    hide text with fade
    return


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Arina = Character("Arina", color="#fff")
define Cecep = Character("Cecep", color="#fff")
define Edgar = Character("Edgar", color="#fff")
define Eline = Character("Eline", color="#fff")
define Kebin = Character("Kebin", color="#fff")
define Nanda = Character("Nanda", color="#fff")
define PakYusuf = Character("Pak Yusuf", color="#fff")
define Semuanya = Character("Semuanya", color="#fff")
define Shella = Character("Shella", color="#fff")
define Yoga = Character("Yoga", color="#fff")
define Zara = Character("Zara", color="#fff")

# The game starts here.

label start:

    play music "audio/music/dialog1.mpeg"

    play sound "audio/sfx/schoolbell.mp3"

    define gui.text_line_spacing = 18

    show black

    "{i}{cps=25}Bel istirahat berbunyi{/cps}{/i}"

    scene bg_kelas
    with Dissolve (1)

    show ch_eline_normal:
        xalign 0.5
        yalign -0.01
        zoom 0.8

    Eline "{cps=25}Nan, katanya kamu mau gabung osis ya?{/cps}"

    hide ch_eline_normal
    show ch_zara_kaget:
        xalign 1.10
        yalign -0.01
        zoom 1.170

    Zara "{cps=25}Hah benarkah?{/cps}"

    hide ch_zara_kaget
    show ch_nanda_normal:
        xalign -0.20
        yalign -0.01
        zoom 1.170
    show ch_zara_normal:
        xalign 1.10
        yalign -0.01
        zoom 1.170

    Nanda "{cps=25}Iya, rencananya begitu.{/cps}"
    Nanda "{cps=25}Celia memintaku untuk bergabung.{/cps}"

    hide ch_zara_normal
    show ch_zara_kesal:
        xalign 1.10
        yalign -0.01
        zoom 1.170

    Zara "{cps=25}Gadis itu..{/cps}"

    hide ch_zara_kesal
    show ch_cecep_normal:
        xalign 1.10
        yalign -0.0
        zoom 0.75

    Cecep "{cps=25}Seharusnya kamu Nan yang menjadi ketua osis.{/cps}"

    hide ch_cecep_normal
    show ch_yoga_normal:
        xalign 1.10
        yalign -0.0
        zoom 1.170

    Yoga "{cps=25}Bener tuh, pasti langsung kepilih.{/cps}"

    hide ch_yoga_normal
    show ch_eline_senang:
        xalign 1.10
        yalign -0.01
        zoom 1.170
        
    Eline "{cps=25}Kalian ini pintar menjilat ya..{/cps}"

    show ch_nanda_senang:
        xalign -0.20
        yalign -0.01
        zoom 1.170

    Nanda "{cps=25}Akan susah membagi waktu dengan klub basket jika aku menjadi ketua osis.{/cps}"

    hide ch_nanda_senang
    hide ch_nanda_normal
    hide ch_eline_senang
    show ch_eline_normal:
        xalign 1.10
        yalign -0.01
        zoom 0.735
    show ch_zara_normal:
        xalign -0.20
        yalign -0.01
        zoom 1.170
        xzoom -1

    Eline "{cps=25}Zara kenapa nggak ikut osis sekalian?{/cps}"
    Zara "{cps=25}Untuk apa aku ikut hal semacam itu.{/cps}"

    hide ch_eline_normal
    show ch_eline_senang:
        xalign 1.10
        yalign -0.01
        zoom 1.170
    
    Eline "{cps=25}Yahh padahal kamu cocok menjadi osis.{/cps}"

    hide ch_zara_normal
    show ch_zara_kesal:
        xalign -0.20
        yalign -0.01
        zoom 1.170
        xzoom -1

    Zara "{cps=25}Tentu saja, jika aku serius bahkan Celia tidak bisa melawanku.{/cps}"

    hide ch_eline_senang
    hide ch_zara_kesal

    show ch_kebin_normal:
        xalign 0.5
        yalign -0.02
        zoom 0.7

    Kebin "{cps=25}Yare-yare.{/cps}"

    hide ch_kebin_normal
    show ch_edgar_normal:
        xalign -0.20
        yalign -0.01
        zoom 1.170

    Edgar "{cps=25}Apa yang merasuki mu?{/cps}"

    show ch_kebin_normal:
        xalign 1.10
        yalign -0.02
        zoom 0.73

    Kebin "{cps=25}Bisa-bisanya dia membandingkan dirinya dengan Celia.{/cps}"
    Kebin "{cps=25}Tentu saja Celia-chan lebih unggul.{/cps}"

    hide ch_edgar_normal
    show ch_edgar_ehh:
        xalign -0.20
        yalign -0.01
        zoom 1.170

    Edgar "{cps=25}Sejak kapan kau mulai memujanya?{/cps}"
    Kebin "{cps=25}Apa kamu tidak menyadari sesuatu?{/cps}"

    show black with Dissolve (.3)

    "{i}{cps=25}Kevin mengeluarkan HP dan menunjukkan sesuatu kepadaku.{/cps}{/i}"

    scene sc_wallpaper_kebin1 with Dissolve (.3):
        zoom 1
        yalign 0.5

    Edgar "{cps=25}Lumia? Apa maksudmu?{/cps}"
    Edgar "{cps=25}{i}Kenapa dia menunjukkan karakter dari star impact.{/i}{/cps}"
    Edgar "{cps=25}Coba perhatikan lagi.{/cps}"

    scene sc_wallpaper_kebin2 with Dissolve (.3):
        zoom 1
        yalign 0.5

    scene sc_wallpaper_kebin2 with vpunch:
        zoom 1
        yalign 0.5

    Edgar "{cps=25}Ah kembalikan penglihatanku.{/cps}"
    Kebin "{cps=25}Benar kan apa kataku.{/cps}"
    Kebin "{cps=25}Celia-chan adalah perwujudan nyata dari Lumia-chan.{/cps}"
    Edgar "{cps=25}Chan chan chan bapak kau chan.{/cps}"
    Edgar "{cps=25}Berhenti memanggil nama orang seperti itu.{/cps}"
    Kebin "{cps=25}Memangnya kenapa?{/cps}"
    Edgar "{cps=25}Menggelikan.{/cps}"

    scene bg_kelas
    with Dissolve (.5)

    show ch_edgar_normal:
        xalign -0.20
        yalign -0.01
        zoom 1.170

    Edgar "{cps=25}Ah lupakan saja, ngomong-ngomong nanti pulang sekolah bisa temani aku ke klub musik?{/cps}"

    show ch_kebin_cemberut:
        xalign 1.10
        yalign -0.02
        zoom 1.140

    Kebin "{cps=25}Sore ini tidak bisa, watashi harus pergi ke suatu tempat.{/cps}"

    menu:

        "Paksa Kevin untuk mengantar":
            jump choice1_paksa

        "Bilang kalau ada Sera":
            jump choice1_sera

    label choice1_paksa:

        $ menu_flag = True

        hide ch_edgar_normal
        show ch_edgar_smirk:
            xalign -0.20
            yalign -0.01
            zoom 1.170

        Edgar "{cps=25}Ikutlah ini akan seru.{/cps}"
        Kebin "{cps=25}Tidak bisa ini sangat mendesak, aku akan kehabisan stok nya jika terlambat.{/cps}"

        hide ch_edgar_smirk
        show ch_edgar_normal:
            xalign -0.20
            yalign -0.01
            zoom 1.170

        Edgar "{cps=25}Memangnya kau mau pergi kemana?{/cps}"

        hide ch_kebin_cemberut
        show ch_kebin_normal:
            xalign 1.10
            yalign -0.02
            zoom 0.73

        Kebin "{cps=25}Aku ingin membeli figure Lumia-chan yang limited edition.{/cps}"

        hide ch_edgar_normal
        show ch_edgar_kesal:
            xalign -0.20
            yalign -0.01
            zoom 1.170
        Edgar "{cps=25}Apa bagusnya itu?{/cps}"
        Kebin "{cps=25}Kau tidak akan mengerti.{/cps}"
        Kebin "{cps=25}Figure itu hanya ada 100 di dunia ini.{/cps}"
        Edgar "{cps=25}Baiklah apapun itu{/cps}"
        
        jump choice1_done

    label choice1_sera:

        $ menu_flag = False

        hide ch_edgar_normal
        show ch_edgar_smirk:
            xalign -0.20
            yalign -0.01
            zoom 1.170

        Edgar "{cps=25}Ayolah kau yakin tidak mau ikut?{/cps}"
        Kebin "{cps=25}Tentu saja, ini jauh lebih penting.{/cps}"

        hide ch_edgar_smirk
        show ch_edgar_normal:
            xalign -0.20
            yalign -0.01
            zoom 1.170

        Edgar "{cps=25}Baiklah jika kau tidak mau ikut, padahal disana ada Sera.{/cps}"

        hide ch_kebin_cemberut
        show ch_kebin_normal:
            xalign 1.10
            yalign -0.02
            zoom 1.140


        Kebin "{cps=25}Memangnya kenapa? Watashi hanya setia kepada Celia-chan.{/cps}"
        Edgar "{cps=25}Bukankah kau menyukainya.{/cps}"

        hide ch_kebin_normal
        show ch_kebin_senyum:
            xalign 1.10
            yalign -0.02
            zoom 1.140

        Kebin "{cps=25}Aku tidak ingat pernah bilang begitu.{/cps}"

        hide ch_edgar_normal
        show ch_edgar_kesal:
            xalign -0.20
            yalign -0.01
            zoom 1.170

        Edgar "{cps=25}{i}Bedebah ini berganti waifu dengan sangat cepat.{i}{/cps}"

        hide ch_kebin_senyum
        show ch_kebin_cemberut:
            xalign 1.10
            yalign -0.02
            zoom 1.140

        Kebin "{cps=25}Lagian kenapa tiba-tiba kau ingin pergi ke klub musik.{/cps}"

        hide ch_edgar_kesal
        show ch_edgar_normal:
            xalign -0.20
            yalign -0.01
            zoom 1.170

        Edgar "{cps=25}Sera mengajakku.{/cps}"

        hide ch_kebin_cemberut
        show ch_kebin_senyum:
            xalign 1.10
            yalign -0.02
            zoom 1.140

        Kebin "{cps=25}Sejak kapan kalian begitu dekat?{/cps}"
        Edgar "{cps=25}Aku hanya bertemu dengannya di kantin kemarin.{/cps}"

        hide ch_kebin_senyum
        show ch_kebin_normal:
            xalign 1.10
            yalign -0.02
            zoom 1.140

        Kebin "{cps=25}Hee.. naruhodo{/cps}"
        Kebin "{cps=25}Ganbate ne Edgar-kun ><{/cps}"

        hide ch_edgar_normal
        show ch_edgar_kesal:
            xalign -0.20
            yalign -0.01
            zoom 1.170

        Edgar "{cps=25}Sepertinya dia salah paham{/cps}"

        jump choice1_done

    label choice1_done: 
        Kebin "{cps=25}Lagian kenapa tiba-tiba kau ingin pergi ke klub musik.{/cps}"

        hide ch_edgar_kesal
        show ch_edgar_normal:
            xalign -0.20
            yalign -0.01
            zoom 1.170

        Edgar "{cps=25}Sera mengajakku.{/cps}"

        hide ch_kebin_cemberut
        show ch_kebin_senyum:
            xalign 1.10
            yalign -0.02
            zoom 1.140

        Kebin "{cps=25}Sejak kapan kalian begitu dekat?{/cps}"
        Edgar "{cps=25}Aku hanya bertemu dengannya di kantin kemarin.{/cps}"

        hide ch_kebin_senyum
        show ch_kebin_normal:
            xalign 1.10
            yalign -0.02
            zoom 1.140

        Kebin "{cps=25}Hee.. naruhodo{/cps}"
        Kebin "{cps=25}Ganbate ne Edgar-kun ><{/cps}"

        hide ch_edgar_normal
        show ch_edgar_kesal:
            xalign -0.20
            yalign -0.01
            zoom 1.170

        Edgar "{cps=25}Sepertinya dia salah paham{/cps}"
    
# label start:

#     Edgar "{cps=25}Aku memperhatikan kehidupan berjalan di depan mataku.{/cps}"

#     scene sc edgar jendela:
#         yalign 0.5
#     with Dissolve(.5)

#     Edgar "{cps=25}Semua orang terjebak dalam rutinitas yang sama—senyum palsu, obrolan kosong, dan harapan yang tak pernah terwujud.{/cps}"
#     Edgar "{cps=25}Mereka terlihat bahagia, tapi aku tahu itu semua hanya topeng.{/cps}"
#     Edgar "{cps=25}Mungkin aku memang terasing, tapi setidaknya aku jujur pada diriku sendiri.{/cps}"
#     Edgar "{cps=25}Dalam dunia yang penuh kepalsuan ini, menjadi diriku yang sebenarnya adalah satu-satunya cara untuk bertahan.{/cps}"
#     Edgar "{cps=25}Aku lebih memilih kebencian yang nyata daripada cinta yang dipaksakan.{/cps}"
#     Edgar "{cps=25}Jadi, biarlah mereka merayakan kebahagiaan sementara mereka.{/cps}"
#     Edgar "{cps=25}Aku akan tetap di sini, mengamati, merenung, dan menulis kisahku sendiri.{/cps}"

#     scene bg lorong
#     with Dissolve(.5)
#     "{cps=25}{i}Kami pun segera menuju kelas masing-masing karena pembelajaran akan segera dimulai{/i}{/cps}"

#     scene bg kelas
#     with Dissolve(.5)
#     show arina normal:
#         xalign 0.5
#         yalign -0.01
#         zoom 1.170

#     Arina "{cps=25}Duh.. Sepertinya aku lupa membawa buku pelajaran matematika ku.{/cps}"
#     Shella "{cps=25}Kenapa kamu ceroboh sekali ? Bagaimana kamu bisa lupa ? {/cps}"
#     Arina "{cps=25}Aku kesiangan jadi tidak sempat mengecek kembali tas ku.{/cps}"
#     Shella "{cps=25}Apa kamu bermain game sampai tengah malam lagi?{/cps}"
#     Arina "{cps=25}Iya.. hehe.{/cps}"
#     Shella "{cps=25}Coba minta bergabung dengan sebelahmu.{/cps}"
#     Arina "{cps=25}{i}Yahh Eline tidak masuk.{/i}{/cps}"

#     hide arina normal

#     show edgar normal:
#         xalign -0.20
#         yalign -0.01
#         zoom 1.180


#     Edgar "{cps=25}Aku merasakan hal buruk akan datang.{/cps}"
#     Edgar "{cps=25}{i}Dan yap.{/i}{/cps}"

#     show arina normal:
#         xalign 1.10
#         yalign -0.01
#         zoom 1.170

#     Arina "{cps=25}{i}Huft..{/i} Baiklah.{/cps}"
#     Arina "{cps=25}Edgar aku lupa membawa buku, bolehkah aku bergabung denganmu?{/cps}"

#     menu:

#         "Terima":
#             jump choice1_yes

#         "Tolak":
#             jump choice1_no

#     label choice1_yes:

#         $ menu_flag = True

#         Edgar "{cps=25}Boleh, gabung aja.{/cps}"
#         Arina "{cps=25}Makasih.{/cps}"

#         jump choice1_done

#     label choice1_no:

#         $ menu_flag = False

#         Edgar "{cps=25}{i}Merepotkan.{/i}{/cps}"
#         Arina "{cps=25}Apa kau mengatakan sesuatu?{/cps}"
#         Edgar "{cps=25}Ah bukan apa-apa, gabung aja.{/cps}"
#         Arina "{cps=25}Thanks.{/cps}"

#         jump choice1_done

#     label choice1_done: 
#         hide arina normal
#         hide edgar normal

#         "{i}{cps=25}Panggilan ditujukan kepada Pak Yusuf untuk segera pergi ke ruang guru, Terima Kasih.{/cps}{/i}"
#         show pakyusuf normal:
#             xalign 0.5
#             yalign -0.00
#             zoom 1.180

#         PakYusuf "{cps=25}Saya tinggal sebentar ya anak-anak.{/cps}"

#         hide pakyusuf normal

#         Semuanya "{cps=25}Baik pak.{/cps}"

#         show arina normal:
#             xalign 1.00
#             yalign -0.05 
#             yalign -0.01
#             zoom 1.170


#         Arina "{cps=25}Hoamm {i}menguap.{/i}{/cps}"

#         show edgar normal:
#             xalign 0.00
#             yalign -0.03
#             zoom 1.180

#         Edgar "{cps=25}Kamu kurang tidur kah?{/cps}"
#         Arina "{cps=25}Humm, aku semalam keasikan bermain Star impact.{/cps}"
#         Edgar "{cps=25} Ohh Star impact, kemarin habis update ya?{/cps}"
#         Arina "{cps=25}Iya kemarin aku langsung speedrun quest nya, biar gak kena spoiler.{/cps}"
#         Edgar "{cps=25}Sepertinya kamu udah sepuh.{/cps}"
#         Arina "{cps=25}Tidak juga, aku mah masih pemula.{/cps}"
#         Edgar "{cps=25}Ampun puh.{/cps}"

#         scene edgararina_ngegame:
#             yalign 0.5
#         with Dissolve(.5)

#         Edgar "{cps=25}Kamu bisa bantu aku lawan bos mingguan tatang nggak?{/cps}"
#         Arina "{cps=25}Boleh mana id mu.{/cps}"
#         "{cps=25}{i}Kita pun bermain star impact sampai pak yusuf kembali{/i}.{/cps}"


        
 
#     return
