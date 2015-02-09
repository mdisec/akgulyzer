#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Mehmet Dursun Ince
from argparse import ArgumentParser
from random import choice, randint
import locale

locale.setlocale(locale.LC_ALL, "tr_TR")


class Akgulyzer(object):
    def __init__(self, args):
        """
        Kurucu Akgulyzer
        :param args:
        :return:
        """
        if args.encode:
            self.encode(args.encode)
        elif args.random:
            self.random(args.random)

    def random(self, level):
        """
        Parametre olarak verilen degere gore, en az bir kisi tarafindan gorulmus olan
        Akgul metnini rastgele secer ve ekrana basar.
        :param level:
        :return:
        """
        akgul_db = {
            'low': [
                "Seneye bekleriz. LKD uyelei  lutfen dvet beklemeyin parcasıdı. LKD akadeiik Bilşimin organik bir parcasıdır. Mustafa  Akgul",
                "Aslında  tum  seminerler icin bilmeyene hitap edecek , yeterli detayda, seminmer ozeti isterim. Baslik ve konusmaci ve epostasi belli olduktan sonra  bir 'stub acip,  opemnconf uzeriden girilmesini rica ediyorum.",
                ""
            ],
            'medium': [
                "Bilgisayar Mugendislii/Bilim egitini,  Yürkieyenin yazılım  startejisi ve belki Ümiveristelrde  özgür yzılım kullanımı  konularınd apanel olacak LKD den   konusmaci  istiyoruz.",
                "Okudugunu anlamayanlar ülkesi: katılamayacaklar oln mail atsin diyoruz. su ikiis yanlis gondermis -  cikattmıyoru",
                "bu ucune sşizn kurs iicn ben kabul mektubu  uretip dizne koyacagimsiz  github'a   eklediniz dimi?"
            ],
            'hardcore': ["Erdem Bayer'e Akgül hocadan gelen mesajı okuyanlar anlar.."]
        }
        print choice(akgul_db[level])

    def encode(self, text):
        """
        Temel olarak whitespace'e gore parse edip kelimeleri, uzunluguna gore
        random rotasyona tabi tutar.
        :param text:
        :return:
        """
        ret = ""
        for t in text.split():
            ret += self.__rotate(t, randint(0, len(t))) + " "
        print ret

    def __rotate(self, strg, n):
        """
        Verilen parametreye gore string rotasyonu.
        :param strg:
        :param n:
        :return:
        """
        return strg[n:] + strg[:n]

if __name__ == "__main__":
    parser = ArgumentParser(description="Mustafa Akgül'un askerleriyiz..!")
    parser.add_argument("-e", "--encode", help="Verilen metni Akgüller.")
    parser.add_argument("-r", "--random", choices=['low', 'medium', 'hardcore'], default="low",
                        help="Bilinen Akgül metinlerinden birini rastgele seçer.")
    args = parser.parse_args()
    main = Akgulyzer(args)