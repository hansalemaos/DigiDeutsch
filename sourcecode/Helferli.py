# coding: iso-8859-1 -*-
import configparser
import sys
from itertools import zip_longest
from time import sleep
from deep_translator import GoogleTranslator, LingueeTranslator, PonsTranslator
from keyboard_listener import KeyboardListener, Combo
import pyperclip
import wikipedia
from add_color_print_reg import *
wikipedia.set_lang("de")
import textwrap
from einfuehrung import *
from bs4 import BeautifulSoup
import re
windowsrechner = os.name == "nt"
if windowsrechner:
    add_color_print_to_regedit()

updates_quero_estudar_alemao()



configdatei = "helferli.ini"
config = configparser.ConfigParser()
config.read(configdatei)
txt_temp_datei = str(config["DEFAULT"]["txt_temp_datei"]).strip(""""' """)
tempdatei_mit_text = str(config["DEFAULT"]["tempdatei_mit_text"]).strip(""""' """)
mp3datei = str(config["DEFAULT"]["mp3datei"]).strip(""""' """)
link_to_vlc = '"'+str(config["DEFAULT"]["link_to_vlc"]).strip(""""' """)+'"'
use_german_and = str(config["DEFAULT"]["use_german_and"]).strip(""""' """)
linebreak = int(str(config["DEFAULT"]["linebreak"]).strip(""""' """))
wie_oft_wiederholen = int(str(config["DEFAULT"]["wie_oft_audio_wiederholen"]).strip(""""' """))
wrapper = textwrap.TextWrapper(width=linebreak)


if windowsrechner:
    google_de_to_other_language_kombination_and = str(
        config["WINDOWS"]["google_de_to_other_language_kombination_ctrl_alt_and"]).strip(""""' """)
    google_other_language_to_de_kombination_and = str(
        config["WINDOWS"]["google_other_language_to_de_kombination_ctrl_alt_and"]).strip(""""' """)
    pons_uebersetzung_de_pt_kombination_and = str(
        config["WINDOWS"]["pons_uebersetzung_de_pt_kombination_ctrl_alt_and"]).strip(""""' """)
    pons_uebersetzung_pt_de_kombination_and = str(
        config["WINDOWS"]["pons_uebersetzung_pt_de_kombination_ctrl_alt_and"]).strip(""""' """)
    duden_kombination_and = str(config["WINDOWS"]["duden_kombination_ctrl_alt_and"]).strip(""""' """)
    leo_kombination_and = str(config["WINDOWS"]["leo_kombination_ctrl_alt_and"]).strip(""""' """)
    leo_verben_kombination_and = str(config["WINDOWS"]["leo_verben_kombination_ctrl_alt_and"]).strip(""""' """)
    auf_wikipedia_suchen_kombination_and = str(
        config["WINDOWS"]["auf_wikipedia_suchen_kombination_ctrl_alt_and"]).strip(""""' """)
    google_vorlesen_kombination_and = str(config["WINDOWS"]["google_vorlesen_kombination_ctrl_alt_and"]).strip(""""' """)
    linguee_uebersetzung_kombination_and = str(
        config["WINDOWS"]["linguee_uebersetzung_kombination_ctrl_alt_and"]).strip(""""' """)
    edit_config_file_ctrl_alt_and = str(
        config["WINDOWS"]["edit_config_file_ctrl_alt_and"]).strip(""""' """)

if not windowsrechner:
    google_de_to_other_language_kombination_and = str(
        config["MAC"]["google_de_to_other_language_kombination_cmd_and"]).strip(""""' """)
    google_other_language_to_de_kombination_and = str(
        config["MAC"]["google_other_language_to_de_kombination_cmd_and"]).strip(""""' """)
    pons_uebersetzung_de_pt_kombination_and = str(config["MAC"]["pons_uebersetzung_de_pt_kombination_cmd_and"]).strip(""""' """)
    pons_uebersetzung_pt_de_kombination_and = str(config["MAC"]["pons_uebersetzung_pt_de_kombination_cmd_and"]).strip(""""' """)
    duden_kombination_and = str(config["MAC"]["duden_kombination_cmd_and"]).strip(""""' """)
    leo_kombination_and = str(config["MAC"]["leo_kombination_cmd_and"]).strip(""""' """)
    leo_verben_kombination_and = str(config["MAC"]["leo_verben_kombination_cmd_and"]).strip(""""' """)
    auf_wikipedia_suchen_kombination_and = str(config["MAC"]["auf_wikipedia_suchen_kombination_cmd_and"]).strip(""""' """)
    google_vorlesen_kombination_and = str(config["MAC"]["google_vorlesen_kombination_cmd_and"]).strip(""""' """)
    linguee_uebersetzung_kombination_and = str(config["MAC"]["linguee_uebersetzung_kombination_cmd_and"]).strip(""""' """)



def txtdateien_lesen(file):
    if os.path.exists(file):
        with open(file, mode='rb') as f:
            text = f.read()
    elif not os.path.exists(file):
        text = file
    try:
        dateiohnehtml = (
            b"""<!DOCTYPE html><html><body><p>""" + text + b"""</p></body></html>"""
        )
        soup = BeautifulSoup(dateiohnehtml, "html.parser")
        soup = soup.text
        return soup.strip()
    except Exception as Fehler:
        print(Fehler)

def in_datei_schreiben_und_notepad_oeffnen(translated):
    translated = re.sub(r'.\[0m', '\n', translated)


    with open(txt_temp_datei, mode='w', encoding='utf-8') as datei:
        datei.write(translated)

    if windowsrechner:
        try:
            subprocess.Popen(
                ["notepad.exe", txt_temp_datei], stdout=subprocess.PIPE
            )
        except:
            print(f"File could not be opened!\n\n")
    original = pyperclip.paste()
    woerterliste = wrapper.wrap(text=translated)
    original = wrapper.wrap(text=original)

    tliste = [list(xaaa) for xaaa in zip_longest(*[original, woerterliste])]
    tliste = [[x if x is not None else "" for x in y] for y in tliste]

    drucker.p_pandas_list_dict(tliste, header=[use_german_and, 'de'])
    choice(auswahlliste)("Translated text copied to clipboard!")
    sleep(.5)
    try:
        with open(txt_temp_datei, mode='w', encoding='utf-8') as datei:
            datei.write('')
    except:
        pass

def get_file_path(datei):
    pfad = sys.path
    pfad = [x.replace('/', '\\') + '\\' + datei for x in pfad]
    exists = []
    for p in pfad:
        if os.path.exists(p):
            exists.append(p)
    return list(dict.fromkeys(exists))


def edit_config_file():
    inifile = get_file_path('helferli.ini')[0]
    print(drucker.f.black.brightyellow.italic(f'Trying to open: {inifile}'))
    os.system(f'notepad.exe {inifile}')
    print('Please restart the app for changes to take effect ')


def google_de_pt():
    try:
        deutsches_wort = pyperclip.paste()
        in_datei_schreiben_und_notepad_oeffnen(GoogleTranslator(source='de', target=use_german_and).translate(deutsches_wort))
    except Exception as Fehler:
        print(drucker.f.brightwhite.brightred.bold(str(Fehler)))
def google_pt_de():
    try:
        deutsches_wort = pyperclip.paste()
        in_datei_schreiben_und_notepad_oeffnen(GoogleTranslator(source=use_german_and, target='de').translate(deutsches_wort))
    except Exception as Fehler:
        print(drucker.f.brightwhite.brightred.bold(str(Fehler)))
def linguee_uebersetzung():
    try:
        deutsches_wort = pyperclip.paste()
        in_datei_schreiben_und_notepad_oeffnen(LingueeTranslator(source='de', target=use_german_and).translate(deutsches_wort))
    except Exception as Fehler:
        print(drucker.f.brightwhite.brightred.bold(str(Fehler)))
def pons_uebersetzung_de_pt():
    try:
        deutsches_wort = pyperclip.paste()
        in_datei_schreiben_und_notepad_oeffnen(LingueeTranslator(source='de', target=use_german_and).translate(deutsches_wort))
    except Exception as Fehler:
        print(drucker.f.brightwhite.brightred.bold(str(Fehler)))
def pons_uebersetzung_pt_de():
    try:
        deutsches_wort = pyperclip.paste()
        in_datei_schreiben_und_notepad_oeffnen(PonsTranslator(source=use_german_and, target='de').translate(deutsches_wort))
    except Exception as Fehler:
        print(drucker.f.brightwhite.brightred.bold(str(Fehler)))
def duden():
    try:
        deutsches_wort = str(pyperclip.paste()).strip()
        prozess = subprocess.Popen(['duden', deutsches_wort], stdout=subprocess.PIPE)
        ausgabe, fehler = prozess.communicate()
        woerterbuch_eintrag_duden = txtdateien_lesen(ausgabe)
        mehrereda = re.findall(r'matching\s*words', woerterbuch_eintrag_duden)
        allergebnisse = []
        if any(mehrereda):
            for xx in range(4):
                prozess = subprocess.Popen(['duden', f'-r{xx+1}', deutsches_wort], stdout=subprocess.PIPE)
                ausgabe, fehler = prozess.communicate()
                woerterbuch_eintrag_duden = txtdateien_lesen(ausgabe)
                leer = re.findall(r'with\s*number', str(woerterbuch_eintrag_duden))
                if not any(leer):
                    allergebnisse.append(woerterbuch_eintrag_duden)
            woerterbuch_eintrag_duden = '\n'.join(allergebnisse)
        in_datei_schreiben_und_notepad_oeffnen(woerterbuch_eintrag_duden.strip())
    except Exception as Fehler:
        pass
def leo():
    try:
        deutsches_wort = str(pyperclip.paste()).strip()
        prozess = subprocess.Popen(['leo.exe',  '-l' , use_german_and,  deutsches_wort], stdout=subprocess.PIPE)
        ausgabe, fehler = prozess.communicate()
        woerterbuch_eintrag_leo = txtdateien_lesen(ausgabe)
        in_datei_schreiben_und_notepad_oeffnen(woerterbuch_eintrag_leo.strip())
    except Exception as Fehler:
        print(drucker.f.brightwhite.brightred.bold(str(Fehler)))
def leo_verben():
    try:
        deutsches_wort = str(pyperclip.paste()).strip()
        prozess = subprocess.Popen(['leo.exe',  '-i',  deutsches_wort], stdout=subprocess.PIPE)
        ausgabe, fehler = prozess.communicate()
        woerterbuch_eintrag_leo = txtdateien_lesen(ausgabe)
        in_datei_schreiben_und_notepad_oeffnen(woerterbuch_eintrag_leo.strip())
    except Exception as Fehler:
        print(drucker.f.brightwhite.brightred.bold(str(Fehler)))
def auf_wikipedia_suchen():
    try:
        deutsches_wort = pyperclip.paste()
        wikipedia_ergebnis = wikipedia.summary(deutsches_wort)
        in_datei_schreiben_und_notepad_oeffnen(wikipedia_ergebnis)
    except Exception as Fehler:
        print(drucker.f.brightwhite.brightred.bold(str(Fehler)))

def google_vorlesen():
    try:

        deutsches_wort = str(pyperclip.paste()).strip()
        with open(tempdatei_mit_text, mode='w', encoding='utf-8') as datei:
            datei.write(deutsches_wort)
        kommando_google_stimme = f'gtts-cli --file {tempdatei_mit_text} --lang de --output {mp3datei}'
        os.system(kommando_google_stimme)
        kommando_abspielen_mit_vlc = fr'{link_to_vlc} --input-repeat={wie_oft_wiederholen} -Idummy --play-and-exit {mp3datei}'
        os.system(kommando_abspielen_mit_vlc)
    except Exception as Fehler:
        print(drucker.f.brightwhite.brightred.bold(str(Fehler)))

if windowsrechner:
    mittevariable = ['ctrl','alt']
if not windowsrechner:
    mittevariable = ['cmd']


ausdrucken = [[f'Translate from German to {use_german_and} via Google', '+'.join(mittevariable).strip('+')+ '+'+google_de_to_other_language_kombination_and],
[f'Translate from {use_german_and} to German via Google', '+'.join(mittevariable).strip('+')+ '+'+google_other_language_to_de_kombination_and],
[f'Translate from German to {use_german_and} via PONS', '+'.join(mittevariable).strip('+')+ '+'+pons_uebersetzung_de_pt_kombination_and],
[f'Translate from {use_german_and} to German via PONS', '+'.join(mittevariable).strip('+')+ '+'+pons_uebersetzung_pt_de_kombination_and],
[f'Search on duden.de', '+'.join(mittevariable).strip('+')+ '+'+duden_kombination_and],
[f'Translate from German to {use_german_and} via dict.leo.org', '+'.join(mittevariable).strip('+')+ '+'+leo_kombination_and],
[f'Conjugate verbs via dict.leo.org', '+'.join(mittevariable).strip('+')+ '+'+leo_verben_kombination_and],
[f'Search on German Wikipedia', '+'.join(mittevariable).strip('+')+ '+'+auf_wikipedia_suchen_kombination_and],
[f'Read text in German', '+'.join(mittevariable).strip('+')+ '+'+google_vorlesen_kombination_and],
[f'Translate from German to {use_german_and} via linguee.com', '+'.join(mittevariable).strip('+')+ '+'+linguee_uebersetzung_kombination_and],
              [f'Edit config file', '+'.join(mittevariable).strip('+')+ '+'+edit_config_file_ctrl_alt_and]]




einfuehrung(name='Digi-Deutsch')

drucker.p_pandas_list_dict(ausdrucken, header=['Beschreibung', 'Shortcut'])

combinations = {
'google_de_to_other_language_kombination_and': Combo(mittevariable, google_de_to_other_language_kombination_and, google_de_pt),
'google_other_language_to_de_kombination_and': Combo(mittevariable, google_other_language_to_de_kombination_and, google_pt_de),
'pons_uebersetzung_de_pt_kombination_and': Combo(mittevariable, pons_uebersetzung_de_pt_kombination_and, pons_uebersetzung_de_pt),
'pons_uebersetzung_pt_de_kombination_and': Combo(mittevariable, pons_uebersetzung_pt_de_kombination_and, pons_uebersetzung_pt_de),
'duden_kombination_and': Combo(mittevariable, duden_kombination_and, duden),
'leo_kombination_and': Combo(mittevariable, leo_kombination_and, leo),
'leo_verben_kombination_and': Combo(mittevariable, leo_verben_kombination_and, leo_verben),
'auf_wikipedia_suchen_kombination_and': Combo(mittevariable, auf_wikipedia_suchen_kombination_and, auf_wikipedia_suchen),
'google_vorlesen_kombination_and': Combo(mittevariable, google_vorlesen_kombination_and, google_vorlesen),
'linguee_uebersetzung_kombination_and': Combo(mittevariable, linguee_uebersetzung_kombination_and, linguee_uebersetzung),
'edit_config_file_ctrl_alt_and': Combo(mittevariable, edit_config_file_ctrl_alt_and, edit_config_file)


}


keyboard_listener = KeyboardListener(combinations=combinations)
keyboard_listener.run()

