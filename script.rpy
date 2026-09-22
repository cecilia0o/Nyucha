# =========================================================
# SPLASH SCREEN
# =========================================================

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
# The game starts here.

# =========================================================
# GAME START
# =========================================================

label start:

    play music "audio/music/dialog1.mpeg"
    play sound "audio/sfx/schoolbell.mp3"

    show black

    "{i}{cps=25}Bel istirahat berbunyi{/cps}{/i}"


    # =====================================================
    # CLASSROOM
    # =====================================================

    scene bg_kelas with Dissolve(1)

    show ch_eline_normal at center_char

    Eline "{cps=25}Nan, katanya kamu mau gabung osis ya?{/cps}"


    hide ch_eline_normal
    show ch_zara_kaget at right_char

    Zara "{cps=25}Hah benarkah?{/cps}"


    hide ch_zara_kaget
    show ch_nanda_normal at left_char
    show ch_zara_normal at right_char

    Nanda "{cps=25}Iya, rencananya begitu.{/cps}"
    Nanda "{cps=25}Celia memintaku untuk bergabung.{/cps}"


    hide ch_zara_normal
    show ch_zara_kesal at right_char

    Zara "{cps=25}Gadis itu..{/cps}"


    hide ch_zara_kesal
    show ch_cecep_normal at cecep_pos

    Cecep "{cps=25}Seharusnya kamu Nan yang menjadi ketua osis.{/cps}"


    hide ch_cecep_normal
    show ch_yoga_normal at right_char

    Yoga "{cps=25}Bener tuh, pasti langsung kepilih.{/cps}"


    hide ch_yoga_normal
    show ch_eline_senang at right_char

    Eline "{cps=25}Kalian ini pintar menjilat ya..{/cps}"

    show ch_nanda_senang at left_char

    Nanda "{cps=25}Akan susah membagi waktu dengan klub basket jika aku menjadi ketua osis.{/cps}"


    hide ch_nanda_senang
    hide ch_nanda_normal
    hide ch_eline_senang

    show ch_eline_normal at eline_small
    show ch_zara_normal at left_char_flip

    Eline "{cps=25}Zara kenapa nggak ikut osis sekalian?{/cps}"
    Zara "{cps=25}Untuk apa aku ikut hal semacam itu.{/cps}"


    hide ch_eline_normal
    show ch_eline_senang at right_char

    Eline "{cps=25}Yahh padahal kamu cocok menjadi osis.{/cps}"


    hide ch_zara_normal
    show ch_zara_kesal at left_char_flip

    Zara "{cps=25}Tentu saja, jika aku serius bahkan Celia tidak bisa melawanku.{/cps}"


    hide ch_eline_senang
    hide ch_zara_kesal


    # =====================================================
    # KEBIN & EDGAR
    # =====================================================

    show ch_kebin_normal at kebin_center

    Kebin "{cps=25}Yare-yare.{/cps}"


    hide ch_kebin_normal
    show ch_edgar_normal at left_char

    Edgar "{cps=25}Apa yang merasuki mu?{/cps}"

    show ch_kebin_normal at kebin_pos

    Kebin "{cps=25}Bisa-bisanya dia membandingkan dirinya dengan Celia.{/cps}"
    Kebin "{cps=25}Tentu saja Celia-chan lebih unggul.{/cps}"


    hide ch_edgar_normal
    show ch_edgar_ehh at left_char

    Edgar "{cps=25}Sejak kapan kau mulai memujanya?{/cps}"
    Kebin "{cps=25}Apa kamu tidak menyadari sesuatu?{/cps}"


    # =====================================================
    # KEBIN'S PHONE
    # =====================================================

    show black with Dissolve(.3)

    "{i}{cps=25}Kevin mengeluarkan HP dan menunjukkan sesuatu kepadaku.{/cps}{/i}"


    scene sc_wallpaper_kebin1 with Dissolve(.3):
        zoom 1
        yalign 0.5

    Edgar "{cps=25}Lumia? Apa maksudmu?{/cps}"
    Edgar "{cps=25}{i}Kenapa dia menunjukkan karakter dari star impact.{/i}{/cps}"
    Edgar "{cps=25}Coba perhatikan lagi.{/cps}"


    scene sc_wallpaper_kebin2 with Dissolve(.3):
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


    # =====================================================
    # BACK TO CLASS
    # =====================================================

    scene bg_kelas with Dissolve(.5)

    show ch_edgar_normal at left_char

    Edgar "{cps=25}Ah lupakan saja, ngomong-ngomong nanti pulang sekolah bisa temani aku ke klub musik?{/cps}"


    show ch_kebin_cemberut at kebin_pos

    Kebin "{cps=25}Sore ini tidak bisa, watashi harus pergi ke suatu tempat.{/cps}"


    # =====================================================
    # CHOICE 1
    # =====================================================

    menu:

        "Paksa Kevin untuk mengantar":
            jump choice1_paksa

        "Bilang kalau ada Sera":
            jump choice1_sera


# =========================================================
# CHOICE 1 - PAKSA KEVIN
# =========================================================

label choice1_paksa:

    $ menu_flag = True

    hide ch_edgar_normal
    show ch_edgar_smirk at left_char

    Edgar "{cps=25}Ikutlah ini akan seru.{/cps}"
    Kebin "{cps=25}Tidak bisa ini sangat mendesak, aku akan kehabisan stok nya jika terlambat.{/cps}"


    hide ch_edgar_smirk
    show ch_edgar_normal at left_char

    Edgar "{cps=25}Memangnya kau mau pergi kemana?{/cps}"


    hide ch_kebin_cemberut
    show ch_kebin_normal at kebin_pos

    Kebin "{cps=25}Aku ingin membeli figure Lumia-chan yang limited edition.{/cps}"


    hide ch_edgar_normal
    show ch_edgar_kesal at left_char

    Edgar "{cps=25}Apa bagusnya itu?{/cps}"
    Kebin "{cps=25}Kau tidak akan mengerti.{/cps}"
    Kebin "{cps=25}Figure itu hanya ada 100 di dunia ini.{/cps}"
    Edgar "{cps=25}Baiklah apapun itu{/cps}"


    jump choice1_done


# =========================================================
# CHOICE 1 - SERA
# =========================================================

label choice1_sera:

    $ menu_flag = False

    hide ch_edgar_normal
    show ch_edgar_smirk at left_char

    Edgar "{cps=25}Ayolah kau yakin tidak mau ikut?{/cps}"
    Kebin "{cps=25}Tentu saja, ini jauh lebih penting.{/cps}"


    hide ch_edgar_smirk
    show ch_edgar_normal at left_char

    Edgar "{cps=25}Baiklah jika kau tidak mau ikut, padahal disana ada Sera.{/cps}"


    hide ch_kebin_cemberut
    show ch_kebin_normal at kebin_pos

    Kebin "{cps=25}Memangnya kenapa? Watashi hanya setia kepada Celia-chan.{/cps}"
    Edgar "{cps=25}Bukankah kau menyukainya.{/cps}"


    hide ch_kebin_normal
    show ch_kebin_senyum at kebin_pos

    Kebin "{cps=25}Aku tidak ingat pernah bilang begitu.{/cps}"


    hide ch_edgar_normal
    show ch_edgar_kesal at left_char

    Edgar "{cps=25}{i}Bedebah ini berganti waifu dengan sangat cepat.{/i}{/cps}"


    hide ch_kebin_senyum
    show ch_kebin_cemberut at kebin_pos

    Kebin "{cps=25}Lagian kenapa tiba-tiba kau ingin pergi ke klub musik.{/cps}"


    hide ch_edgar_kesal
    show ch_edgar_normal at left_char

    Edgar "{cps=25}Sera mengajakku.{/cps}"


    hide ch_kebin_cemberut
    show ch_kebin_senyum at kebin_pos

    Kebin "{cps=25}Sejak kapan kalian begitu dekat?{/cps}"
    Edgar "{cps=25}Aku hanya bertemu dengannya di kantin kemarin.{/cps}"


    hide ch_kebin_senyum
    show ch_kebin_normal at kebin_pos

    Kebin "{cps=25}Hee.. naruhodo{/cps}"
    Kebin "{cps=25}Ganbate ne Edgar-kun ><{/cps}"


    hide ch_edgar_normal
    show ch_edgar_kesal at left_char

    Edgar "{cps=25}Sepertinya dia salah paham{/cps}"


    jump choice1_done


# =========================================================
# COMMON ROUTE
# =========================================================

label choice1_done:

    Kebin "{cps=25}Lagian kenapa tiba-tiba kau ingin pergi ke klub musik.{/cps}"


    hide ch_edgar_kesal
    show ch_edgar_normal at left_char

    Edgar "{cps=25}Sera mengajakku.{/cps}"


    hide ch_kebin_cemberut
    show ch_kebin_senyum at kebin_pos

    Kebin "{cps=25}Sejak kapan kalian begitu dekat?{/cps}"
    Edgar "{cps=25}Aku hanya bertemu dengannya di kantin kemarin.{/cps}"


    hide ch_kebin_senyum
    show ch_kebin_normal at kebin_pos

    Kebin "{cps=25}Hee.. naruhodo{/cps}"
    Kebin "{cps=25}Ganbate ne Edgar-kun ><{/cps}"


    hide ch_edgar_normal
    show ch_edgar_kesal at left_char

    Edgar "{cps=25}Sepertinya dia salah paham{/cps}"

    return