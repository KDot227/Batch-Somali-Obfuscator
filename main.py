import time
import os

# feel free to change most of the values that ARENT IN ANY FUNCTIONS or __author__ (mainly the chinese var and a few other things. Have fun looking)

try:
    from rich.progress import Progress, track
    from zipfile import ZipFile
    from random import randint
    from pystyle import *
    import colorama
    import requests
    import random
    import string
    import re
except:
    print(
        "You don't have the required modules installed. Please run the setup.bat file to fix this."
    )
    time.sleep(5)
    os._exit(1)

colorama.deinit()

__author__ = "K.Dot#4044 and Godfather"

cesar_val = randint(1, 13)


def caesar_cipher_rotations(rotation):
    """Generates the Caesar cipher for a given rotation value."""
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    rotated_alphabet = alphabet[rotation:] + alphabet[:rotation]
    cipher_pairs = [
        f'set "{rotated_alphabet[i]}={c}" && ' for i, c in enumerate(alphabet)
    ]

    return "".join(cipher_pairs)


def caesar_cipher_rotations_upper(rotation):
    """Generates the Caesar cipher for a given rotation value. (CAPITAL LETTERS ONLY)"""
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    rotated_alphabet = alphabet[rotation:] + alphabet[:rotation]
    cipher_pairs = [
        f'set "{rotated_alphabet[i]}1={c}" && ' for i, c in enumerate(alphabet)
    ]

    return "".join(cipher_pairs)


together = caesar_cipher_rotations(cesar_val) + caesar_cipher_rotations_upper(cesar_val)
together = together[:-4]


# average W batch thing where u get a error every line :skull:
chinese = False

if chinese:
    chinese_characters = "苑范腕勝滕贖值債價償責直真賭哀衰衷袁忠棄業停亨享亭亮閏闊閒闌聞門閂閃閉開閑間閘閡閣閥閨閩閱閹閻闃闔闕闖關闡募幕慕壞壤讓鑲"
else:
    chinese_characters = string.ascii_letters + string.digits

code = f"""@echo off
{together}
chcp 65001 > nul
"""
if (
    __author__
    != "\x4b\x2e\x44\x6f\x74\x23\x34\x30\x34\x34\x20\x61\x6e\x64\x20\x47\x6f\x64\x66\x61\x74\x68\x65\x72"
):
    os._exit(0)
banner = Center.XCenter(
    """
███████╗ ██████╗ ███╗   ███╗ █████╗ ██╗     ██╗███████╗██╗   ██╗███████╗ ██████╗ █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║     ██║██╔════╝██║   ██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████╗██║   ██║██╔████╔██║███████║██║     ██║█████╗  ██║   ██║███████╗██║     ███████║   ██║   ██║   ██║██████╔╝
╚════██║██║   ██║██║╚██╔╝██║██╔══██║██║     ██║██╔══╝  ██║   ██║╚════██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
███████║╚██████╔╝██║ ╚═╝ ██║██║  ██║███████╗██║██║     ╚██████╔╝███████║╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝      ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
 Made by Godfather and K.Dot#4044\n\n
"""
)

options = (
    r"""
[1] Level 1 (Recommended to use AFTER 2) (Rot-x method)
[2] Level 2 (More Variable replacement)
[3] Level 3 (Encoding trick by changing first 2 bytes)
[4] Level 4 (NOTE: Don't end your files with exit when its done with this command or it might break. (same with pause))
[5] Level 5 (NOTE: THIS WAS NOT MADE BY ME IT WAS MADE BY https://www.dostips.com/forum/memberlist.php?mode=viewprofile&u=2258 W mans btw) (If u really wanna be mean use Ultimate first lmao)
[clean] cleans the code to try and fix any common errors (FIXES BUILT IN VARIABLES)
[all] does 1, 2, 3 and clean
[fud] makes it undetectable by everything on virustotal

[ultimate] The Ultimate batch obfuscation (ultimate obf for someone who want's to make the person deobfuscating wanna off themselves)

[embed] Embeds powershell code in a batch file. (they run bat file but it reruns as ps1/powershell)
[exe] Simple Bat2Exe with self extracting zip (usually low detections too)
[exe2] Second method for Bat2Exe (usually low detections but may increase over time)
[COMING SOON] [exe3] Third method for Bat2Exe (100% fud)
[ONELINE] I did it

[?] (If you want to use built in variables such as %~dp0 etc wrap them in percent signes then run the clean mode afterwards.)
"""
    + "\n\n"
)


class AutoUpdate:
    def __init__(self):
        self.code = (
            "https://raw.githubusercontent.com/KDot227/Somalifuscator/main/main.py"
        )
        self.bypass = False

        try:
            username = os.getlogin()
            if username == "this1":
                self.bypass = True
            self.update()
        except OSError:
            self.bypass = True

    def update(self):
        if not self.bypass:
            print("Checking for updates...")
            code = requests.get(self.code, timeout=10).text
            with open(__file__, "r", encoding="utf-8") as f:
                main_code = f.read()
            if code != main_code:
                print("Updating...")
                with open(__file__, "w", encoding="utf-8") as f:
                    f.write(code)
                os.startfile(__file__)
                os._exit(0)
            else:
                print("No updates found!")


class Main:
    def __init__(self):
        # if u on linux kys
        # nvm I'm on linux now I gotta fix this
        os.system("cls" if os.name == "nt" else "clear")
        print(Colorate.Vertical(Colors.purple_to_blue, banner, 2))
        self.carrot = False
        self.label = False
        # This is so the fud mode doesn't show the first time it's ran
        self.down = False
        self.file = Write.Input("File to obfuscate -> ", Colors.green, interval=0.05)
        if os.path.exists(self.file):
            print(Colorate.Vertical(Colors.purple_to_blue, options, 2))
            self.level = Write.Input(
                "What level of Obfuscation do you want? -> ",
                Colors.green,
                interval=0.05,
            )
            self.level = self.level.lower()
            self.level_dict = {
                "1": self.level1,
                "2": self.level2,
                "3": self.level3,
                "4": self.level4,
                "5": self.level5,
                "clean": self.clean,
                "all": self.all,
                "fud": self.fud,
                "ultimate": self.ultimate,
                "embed": self.embed,
                "exe": self.bat2exe,
                "exe2": self.bat2exe2,
                "oneline": self.oneline,
            }

            pick = self.level_dict.get(self.level)
            if pick is not None:
                self.mixer()
                pick()
            else:
                print("Invalid option")
                time.sleep(3)
                Main()
        else:
            print(Colors.red + "That file does not exist!" + Colors.reset)
            time.sleep(3)
            Main()

    @staticmethod
    def make_random_string():
        length = randint(5, 7)
        return "".join(
            random.choice(
                # Batch has a specific issue with characters that aren't in the normal ASCII table cause if u got them in a variable it will make the variable explode. I fixed this before by changing the chcp to 65001 but sometimes that wouldn't fix things
                # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZḆḞԍǏƘԸɌȚЦѠƳȤѧćễļṃŉᵲừŵź☠☢☣卐"
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            )
            for i in range(length)
        )

    @staticmethod
    def make_random_label_no_working():
        # 911 lol
        length = random.choice([9, 11])
        return "".join(random.choice(chinese_characters) for i in range(length))

    @staticmethod
    def make_left_to_right_string():
        # Change if u want
        length = 1
        # left to right unicode things
        return "".join("‮" for i in range(length))

    def random_dead_code(self, entire_array):

        dead_code = [
            "echo Best Batch Obfuscated By KDot and Godfather\n",
            "if 0 == 0 (echo Best Batch Obfuscated By KDot and Godfather)\n",
            f"set KDOT={self.fake_KDOT()}\n",
            f"{self.fake_ceaser_cipher()}\n",
            f"{self.fake_ceaser_cipher_obfuscated()}\n",
        ]
        for array in entire_array:
            if randint(0, 3) == 3:
                option = random.choice(dead_code)
                scated = self.obf_oneline(option)
                new_string = "".join(scated)
                new_string = [new_string]
                entire_array.insert(entire_array.index(array), new_string)

        return entire_array

    @staticmethod
    def fake_ceaser_cipher():
        together = caesar_cipher_rotations(cesar_val) + caesar_cipher_rotations_upper(
            cesar_val
        )
        together = together[:-4]
        return together

    def fake_ceaser_cipher_obfuscated(self):
        cipher = self.fake_ceaser_cipher()
        obfuscated = self.obf_oneline(cipher)
        return obfuscated

    def fake_KDOT(self):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        random_order = "".join(random.sample(characters, len(characters)))
        return random_order

    @staticmethod
    def obf_oneline(line):
        final_string = ""
        for word in line.split(" "):
            if word.startswith("%"):
                final_string += word + " "
                continue
            if word.find("%~") != -1:
                final_string += word + " "
                continue
            else:
                for char in word:
                    public = r"C:\Users\Public"
                    weird = r"C:\Program Files (x86)\Common Files"
                    program_1 = r"C:\Program Files"
                    program_2 = r"C:\Program Files (x86)"
                    psmodule_path = r"%ProgramFiles%\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules"
                    if char in program_1:
                        final_string += f"%programfiles:~{program_1.index(char)},1%"
                    elif char in program_2:
                        final_string += (
                            f"%programfiles(x86):~{program_2.index(char)},1%"
                        )
                    elif char in public:
                        final_string += f"%public:~{public.index(char)},1%"
                    elif char in weird:
                        final_string += (
                            f"%CommonProgramFiles(x86):~{weird.index(char)},1%"
                        )
                    elif char in psmodule_path:
                        new = psmodule_path.index(char)
                        # Why do we have to add 2? I have no fucking idea lmao
                        final_string += f"%PSModulePath:~{new + 2},1%"
                    else:
                        final_string += char
                final_string += " "

        return final_string

    def simple(self, char):
        unicode = True
        if unicode:
            choices = [self.make_random_string(), self.make_left_to_right_string()]
        else:
            choices = [self.make_random_string()]
        return f"%{random.choice(choices)}%{char}%{random.choice(choices)}%"

    def caesar_cipher_rotation(self, letter):
        """Returns the Caesar cipher rotation for a given letter and rotation value."""
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        letter_index = alphabet.index(letter.lower())
        rotated_alphabet = alphabet[cesar_val:] + alphabet[:cesar_val]
        rotated_letter = rotated_alphabet[letter_index]

        return rotated_letter

    def caesar_cipher_rotation_UPPER(self, letter):
        """Returns the Caesar cipher rotation for a given letter and rotation value."""
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        letter_index = alphabet.index(letter.upper())
        rotated_alphabet = alphabet[cesar_val:] + alphabet[:cesar_val]
        rotated_letter = rotated_alphabet[letter_index]

        return rotated_letter

    def mixer(self):
        original_file = self.file
        with open("mixer.bat", "w") as f:
            f.write(code)
        self.file = "mixer.bat"
        self.fud()
        with open("mixer.bat.fud.bat", "r", encoding="utf-8") as f:
            self.code_new = f.read()
        os.remove("mixer.bat")
        os.remove("mixer.bat.fud.bat")
        self.file = original_file

    def level1(self):
        carrot = False
        var = False
        try:
            os.remove(f"{self.file}.level1.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8") as f:
            data = f.readlines()
        with open(f"{self.file}.level1.bat", "a+", encoding="utf-8") as f:
            f.write(self.code_new)
            for line in track(
                data, description="[bold green]Obfuscating", total=len(data)
            ):
                if line.startswith(":") and not line.startswith("::"):
                    f.write(line)
                    continue
                for char in line:
                    if char == ">":
                        f.write(char)
                    elif char == "^":
                        f.write(char)
                        carrot = True
                    elif carrot == True:
                        f.write(char)
                        carrot = False
                    else:
                        if char == "%":
                            var = not var
                            f.write(char)

                        elif var == True:
                            f.write(char)

                        elif "\n" in char:
                            f.write(char)

                        else:
                            random = self.make_random_string()
                            if char in string.ascii_letters:
                                if char.islower():
                                    coded0 = self.caesar_cipher_rotation(char)
                                    coded = coded0.replace(coded0, f"%{coded0}%")
                                    f.write(f"{coded}%{random}%")
                                else:
                                    coded0 = self.caesar_cipher_rotation_UPPER(char)
                                    coded = coded0.replace(coded0, f"%{coded0}1%")
                                    f.write(f"{coded}%{random}%")
                            else:
                                f.write(f"{char}%{random}%")

    def level2(self):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        random_order = "".join(random.sample(characters, len(characters)))
        carrot = False
        var = False
        try:
            os.remove(f"{self.file}.level2.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8") as f:
            data = f.readlines()
        with open(f"{self.file}.level2.bat", "a+", encoding="utf-8") as f:
            f.write(f"set KDOT={random_order}\nchcp 65001 > nul\n")
            for line in track(
                data, description="[bold green]Obfuscating", total=len(data)
            ):
                if line.startswith(":") and not line.startswith("::"):
                    f.write(line)
                    continue
                for char in line:
                    if char == ">":
                        f.write(char)
                    elif char == "^":
                        f.write(char)
                        carrot = True
                    elif carrot == True:
                        f.write(char)
                        carrot = False
                    else:
                        if char == "%":
                            var = not var
                            f.write(char)

                        elif var == True:
                            f.write(char)

                        elif "\n" in char:
                            f.write(char)

                        else:
                            if char in string.ascii_letters:
                                vard = f"%KDOT:~{random_order.index(char)},1%"
                                f.write(vard)
                            else:
                                f.write(char)

    def level3(self):
        out_hex = []

        # lowkey overkill lmao
        out_hex.extend(["FF", "FE", "0A", "0D"])
        with open(f"{self.file}", "rb") as f:
            penis = f.read()

        out_hex.extend(["{:02X}".format(b) for b in penis])

        with open(f"{self.file}.level3.bat", "wb") as f:
            for i in out_hex:
                f.write(bytes.fromhex(i))

    def clean(self):
        with open(self.file, "r", encoding="utf-8") as f:
            contents = f.read()
        with open(f"{self.file}.cleaned.bat", "a+", encoding="utf-8") as f:
            # if there are any others that people use please make a pr and add them.
            batch_vars = [
                "%~dp0",
                "%~f0",
                "%~n0",
                "%~x0",
                "%~dpnx0",
            ]
            batch_vars_to_replace = [
                r"%~dp0%",
                r"%~f0%",
                r"%~n0%",
                r"%~x0%",
                r"%~dpnx0%",
            ]
            for i in range(len(batch_vars)):
                contents = contents.replace(batch_vars_to_replace[i], batch_vars[i])
            f.write(contents)

    def all(self):
        names = []
        self.level2()
        self.file = f"{self.file}.level2.bat"
        names.append(self.file)
        self.level1()
        self.file = f"{self.file}.level1.bat"
        names.append(self.file)
        self.clean()
        self.file = f"{self.file}.cleaned.bat"
        names.append(self.file)
        self.level3()
        os.rename(f"{self.file}.level3.bat", "FINAL.bat")
        for name in names:
            os.remove(name)
        print("FINAL.bat is the finished product!")
        time.sleep(5)
        os._exit(0)

    def fud(self):
        carrot = False
        var = False
        try:
            os.remove(f"{self.file}.fud.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8") as f:
            data = f.readlines()
        with open(f"{self.file}.fud.bat", "a+", encoding="utf-8") as f:
            f.write("::Made by K.Dot and Godfather\n")
            if self.down == False:
                for line in data:
                    if line.startswith(":") and not line.startswith("::"):
                        f.write(line)
                        continue
                    for char in line:
                        if char == ">":
                            f.write(char)
                        elif char == "^":
                            f.write(char)
                            carrot = True
                        elif carrot == True:
                            f.write(char)
                            carrot = False
                        else:
                            if char == "%":
                                var = not var
                                f.write(char)
                            elif var == True:
                                f.write(char)
                            elif "\n" in char:
                                f.write(char)
                            else:
                                random = self.make_random_string()
                                f.write(f"{char}%{random}%")
            else:
                for line in track(
                    data, description="[bold green]Obfuscating", total=len(data)
                ):
                    if line.startswith(":") and not line.startswith("::"):
                        f.write(line)
                        continue
                    for char in line:
                        if char == ">":
                            f.write(char)
                        elif char == "^":
                            f.write(char)
                            carrot = True
                        elif carrot == True:
                            f.write(char)
                            carrot = False
                        else:
                            if char == "%":
                                var = not var
                                f.write(char)
                            elif var == True:
                                f.write(char)
                            elif "\n" in char:
                                f.write(char)
                            else:
                                random = self.make_random_string()
                                f.write(f"{char}%{random}%")
        self.down = not self.down

    def ultimate(self) -> None:
        with Progress() as progress:
            task1 = progress.add_task("[bold green]Searching through file", total=100)
            task1andhalf = progress.add_task("[bold green]Obfuscating", total=100)
            task2 = progress.add_task("[bold green]Adding Anti Echo", total=100)
            task3 = progress.add_task("[bold green]Cleaning Obfuscated Code", total=100)
            task4 = progress.add_task(
                "[bold green]Cleaning up Echo Commands", total=100
            )
            task5 = progress.add_task(
                "[bold green]Writing Out-Bytes to File", total=100
            )
            try:
                os.remove(f"{self.file}.ultimate.bat")
            except:
                pass
            # cool thing
            # mshta vbscript:execute("CreateObject(""Scripting.FileSystemObject"").GetStandardStream(1).Write(Chr(89) & Chr(111)& Chr(117) & Chr(114) & Chr(32) & Chr(109) & Chr(97) & Chr(109) & Chr(97) & Chr(32) ):Close")|more
            # ultimate mode
            with open(self.file, "r", encoding="utf-8") as f:
                data = f.readlines()

            # This took way longer than it should have

            new_lines = []
            i = 0
            while i < len(data):
                line = data[i].strip()

                if line.endswith("("):
                    while not line.endswith(")"):
                        i += 1
                        next_line = data[i].strip()
                        # Add '&' between lines cause it can't just do stuff like allat
                        line += " & " + next_line

                    line = line.replace("\n", " ").replace("\r", "")
                    line = " ".join(line.split())

                    # regex cause im a RE tard
                    # that was funny asf ngl
                    matches = re.findall(r"\((.*?)\)", line)
                    for match in matches:
                        modified_match = match[2:-2]
                        line = line.replace(match, modified_match)

                if line:
                    new_lines.append(line)
                i += 1

            data = new_lines

            env_vars = [
                r"%ALLUSERSPROFILE%",
                r"%APPDATA%",
                r"%CD%",
                r"%CMDCMDLINE%",
                r"%CMDEXTVERSION%",
                r"%COMPUTERNAME%",
                r"%COMSPEC%",
                r"%DATE%",
                r"%ERRORLEVEL%",
                r"%HOMEDRIVE%",
                r"%HOMEPATH%",
                r"%NUMBER_OF_PROCESSORS%",
                r"%OS%",
                r"%PATH%",
                r"%PATHEXT%",
                r"%PROCESSOR_ARCHITECTURE%",
                r"%PROCESSOR_LEVEL%",
                r"%PROCESSOR_REVISION%",
                r"%PROMPT%",
                r"%RANDOM%",
                r"%SYSTEMDRIVE%",
                r"%SYSTEMROOT%",
                r"%TMP%",
                r"%TEMP%",
                r"%TIME%",
                r"%USERDOMAIN%",
                r"%USERNAME%",
                r"%USERPROFILE%",
                r"%WINDIR%",
                r"%0",
                r"%1",
                r"%2",
                r"%3",
                r"%4",
                r"%5",
                r"%6",
                r"%7",
                r"%8",
                r"%9",
                r"%*",
                r"%~dp0",
                r"%~dp1",
                r"%~dp2",
                r"%~dp3",
                r"%~dp4",
                r"%~dp5",
                r"%~dp6",
                r"%~dp7",
                r"%~dp8",
                r"%~dp9",
                r"%~f0",
                r"%~f1",
                r"%~f2",
                r"%~f3",
                r"%~f4",
                r"%~f5",
                r"%~f6",
                r"%~f7",
                r"%~f8",
                r"%~f9",
                r"%~nx0",
                r"%~nx1",
                r"%~nx2",
                r"%~nx3",
                r"%~nx4",
                r"%~nx5",
                r"%~nx6",
                r"%~nx7",
                r"%~nx8",
                r"%~nx9",
                r"%~s0",
                r"%~s1",
                r"%~s2",
                r"%~s3",
                r"%~s4",
                r"%~s5",
                r"%~s6",
                r"%~s7",
                r"%~s8",
                r"%~s9",
                r"%~t0",
                r"%~t1",
                r"%~t2",
                r"%~t3",
                r"%~t4",
                r"%~t5",
                r"%~t6",
                r"%~t7",
                r"%~t8",
                r"%~t9",
                r"%~x0",
                r"%~x1",
                r"%~x2",
                r"%~x3",
                r"%~x4",
                r"%~x5",
                r"%~x6",
                r"%~x7",
                r"%~x8",
                r"%~x9",
                r"%~a0",
                r"%~dpn0",
                r"%~dpnx0",
            ]

            self.used_env_vars = []

            for env_var in env_vars:
                if env_var in data:
                    self.used_env_vars.append(env_var)

            progress.update(task1, advance=100)
            with open(f"{self.file}.ultimate.bat", "a+", encoding="utf-8") as f:
                f.write("::Made by K.Dot and Godfather\n")
                f.write(self.code_new)
                characters = (
                    "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                )
                random_order = "".join(random.sample(characters, len(characters)))
                f.write(f"set KDOT={random_order}\n")
                # for line in track(
                #    data, description="[bold green]Obfuscating", total=len(data)
                # ):
                regex_bat = re.compile(r"\w+=[^=]*%\w+%\b|\w+=[^=]*%\w+%\B")
                for line in data:
                    progress.update(task1andhalf, advance=100 / len(data))
                    random_bool = random.choice([True, False])
                    if line.startswith("::"):
                        f.write(line)
                        continue
                    elif line.startswith(":"):
                        f.write(line)
                        continue
                    else:
                        if random_bool == True:
                            f.write(";")
                        for word in line.split():
                            if word.startswith("%") or word.startswith("!"):
                                f.write(word + " ")
                                continue
                            elif re.match(regex_bat, word):
                                # regex be my bae
                                f.write(word + " ")
                                continue
                            else:
                                for char in word:
                                    if char == "\n":
                                        f.write("\n")
                                        continue
                                    elif char == " ":
                                        f.write(" ")
                                        continue
                                    else:
                                        # random_obf = [self.ran1(char), self.ran2(char, random_order), self.ran3(char), self.ran4(char)]
                                        # I'll fix this someday
                                        random_obf = [
                                            self.ran1(char),
                                            # ran 2 is the only thing stopping most deobfuscators since it uses environment variables that nobody knows about
                                            self.ran2(char, random_order),
                                            # self.ran4(char),
                                        ]
                                        f.write(f"{random.choice(random_obf)}")
                                f.write(" ")
                        f.write("\n")
            with open(f"{self.file}.ultimate.bat", "r", encoding="utf-8") as f:
                news = f.readlines()
            news.insert(2, self.obf_oneline(self.first_line_echo_check()))
            messed_up = self.scrambler(news)
            progress.update(task2, advance=100)
            with open(f"{self.file}.ultimate.bat", "w", encoding="utf-8") as f:
                for array in messed_up:
                    for thing in array:
                        f.write(thing.strip() + "\n")
            progress.update(task3, advance=100)
            with open(f"{self.file}.ultimate.bat", "r", encoding="utf-8") as f:
                data = f.readlines()
                for i in range(len(data)):
                    if "echo" in data[i]:
                        data[i] = data[i].replace(
                            "echo", r"%GODFATHER%e%GODFATHER%c%GODFATHER%h%GODFATHER%o"
                        )
            progress.update(task4, advance=100)
            out_hex = self.anti_check_error(code=data)
            with open(f"{self.file}.ultimate.bat", "wb") as f:
                for i in out_hex:
                    f.write(bytes.fromhex(i))
            progress.update(task5, advance=100)

    def ran1(self, char):
        choices = [self.make_random_string(), self.make_random_string()]
        randomed = random.choice(choices)
        if char in string.ascii_letters:
            if char.islower():
                coded0 = self.caesar_cipher_rotation(char)
                coded = coded0.replace(coded0, f"%{coded0}%")
                return f"{coded}%{randomed}%"
            else:
                coded0 = self.caesar_cipher_rotation_UPPER(char)
                coded = coded0.replace(coded0, f"%{coded0}1%")
                return f"{coded}%{randomed}%"
        else:
            return f"{char}%{randomed}%"

    def ran2(self, char, random_order):
        public = r"C:\Users\Public"
        weird = r"C:\Program Files (x86)\Common Files"
        program_1 = r"C:\Program Files"
        program_2 = r"C:\Program Files (x86)"
        psmodule_path = r"%ProgramFiles%\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules"
        # who_even_knows = r"C:\Windows\apppatch\Custom\Custom64"
        if char in program_1:
            return f"%programfiles:~{program_1.index(char)},1%"
        elif char in program_2:
            return f"%programfiles(x86):~{program_2.index(char)},1%"
        # elif char in who_even_knows:
        #    return (
        #        f"%windir%\\apppatch\\Custom\\Custom64:~{who_even_knows.index(char)},1%"
        #    )
        elif char in public:
            return f"%public:~{public.index(char)},1%"
        elif char in weird:
            return f"%CommonProgramFiles(x86):~{weird.index(char)},1%"
        elif char in psmodule_path:
            new = psmodule_path.index(char)
            # Why do we have to add 2? I have no fucking idea lmao
            return f"%PSModulePath:~{new + 2},1%"
        else:
            if char in string.ascii_letters:
                var = f"%KDOT:~{random_order.index(char)},1%"
                return var
            else:
                return char

    def ran3(self, char):
        if char in string.ascii_letters:
            escape = "^"
            return f"{escape}{char}"
        else:
            return char

    def ran4(self, char):
        return char

    @staticmethod
    def generate_math_problem(answer: int):
        # no division since we don't want floats BUT we can use division in the answer since its how you undo multiplication
        operators = ["+", "-"]
        opp1 = random.choice(operators)
        opp2 = random.choice(operators)
        num1 = random.randint(10000, 10000000)
        num2 = random.randint(10000, 10000000)

        problem = f"{answer} {opp1} {num1} {opp2} {num2}"
        ans = eval(problem)

        # make new problem from original answer

        if opp1 == "+":
            opp1 = "-"
        else:
            opp1 = "+"

        if opp2 == "+":
            opp2 = "-"
        else:
            opp2 = "+"

        problem2 = f"{ans} {opp1} {num1} {opp2} {num2}"

        ans2 = eval(problem2)

        batch_version = f"set /a ans={problem2}"

        while ans < 0:

            operators = ["+", "-"]
            opp1 = random.choice(operators)
            opp2 = random.choice(operators)
            num1 = random.randint(10000, 10000000)
            num2 = random.randint(10000, 10000000)

            problem = f"{answer} {opp1} {num1} {opp2} {num2}"
            ans = eval(problem)

            # make new problem from original answer

            if opp1 == "+":
                opp1 = "-"
            else:
                opp1 = "+"

            if opp2 == "+":
                opp2 = "-"
            else:
                opp2 = "+"

            problem2 = f"{ans} {opp1} {num1} {opp2} {num2}"

            ans2 = eval(problem2)

        return problem2, ans2

    def scrambler(self, codeed):
        original_lines = codeed

        for index, line in enumerate(original_lines):
            random_number = random.randint(1, 4)
            if random_number == 1:
                # add a label that doesn't do anything
                label = f":{self.make_random_label_no_working()}\n"
                original_lines.insert(index, label)

        original_lines = [
            item for item in original_lines if item not in [";", "\n", ";\n"]
        ]

        self.dict_thing = {}

        main_list = []

        for index, item in enumerate(original_lines):
            t = self.generate_math_problem(answer=random.randint(100000, 10000000))
            self.dict_thing[item] = [
                t[0],
                t[1],
                index,
            ]

        for index, (key, value) in enumerate(self.dict_thing.items()):
            if index == 0:
                remem = [
                    f";set /a ans={value[0]}\n;{self.random_semi_and_comma(self.obf_oneline('goto'))} :%ans%\n"
                ]
            part_1 = f";:{value[1]}\n"
            part_2 = f";{key}\n"
            try:
                random_t_f = random.choice([True, False])
                if random_t_f:
                    dead = list(self.dict_thing.values())[index + 1][1]
                    random_working_value = random.choice(list(self.dict_thing.values()))
                    while random_working_value[0] == dead:
                        random_working_value = random.choice(
                            list(self.dict_thing.values())
                        )
                    run = self.deadcodes(str(dead), random_working_value)
                    part_3 = f"{run}\n"
                else:
                    maybe_echo_check = random.randint(1, 10)
                    if maybe_echo_check == 1:
                        part_3 = f";set /a ans={list(self.dict_thing.values())[index + 1][0]}\n{self.obf_oneline(self.first_line_echo_check())}\n;{self.random_semi_and_comma(self.obf_oneline('goto'))} :%ans%\n"
                    else:
                        part_3 = f";set /a ans={list(self.dict_thing.values())[index + 1][0]}\n;{self.random_semi_and_comma(self.obf_oneline('goto'))} :%ans%\n"
            except Exception:
                part_3 = (
                    f";{self.random_semi_and_comma(self.obf_oneline('goto'))} :EOF\n"
                )

            main_list.append([part_1, part_2, part_3])

        random.shuffle(main_list)

        main_list = self.bad_labels(main_list)

        main_list = self.random_inserts(main_list)

        main_list = self.random_dead_code(main_list)

        main_list.insert(0, remem)

        return main_list

    def deadcodes(self, labeled, working_val):
        self.rep_num = 0
        # gotta love %random%
        RANNUM = randint(32768, 99999)
        # This is absolute hell for anyone trying to deobfuscate this
        label123 = working_val[0]
        if self.rep_num < 5:
            examples = [
                f";if %random% equ {RANNUM} ( goto :{label123} ) else ( goto :{labeled} )",
                f";if not 0 neq 0 ( goto :{labeled} ) else ( goto :{label123} )",
                f";if exist C:\Windows\System32 ( goto :{labeled} ) else ( goto :{label123} )",
                f";if not %cd% == %cd% ( goto :{label123} ) else ( goto :{labeled} )",
                f";if 0 equ 0 ( goto :{labeled} ) else ( goto :{label123} )",
                f";if exist C:\Windows\System3 ( goto :{label123} ) else ( goto :{labeled} )",
                f";if %cd% == %cd% ( goto :{labeled} ) else ( goto :{label123} )",
                f";if chcp leq 1 ( goto :{label123} ) else ( goto :{labeled} )",
            ]
        else:
            examples = [
                f";if %random% equ {RANNUM} ( goto :{label123} ) else ( goto :{labeled} )",
                f";if not 0 neq 0 ( goto :{labeled} ) else ( goto :{label123} )",
                f";if exist C:\Windows\System32 ( goto :{labeled} ) else ( goto :{label123} )",
                f";if not %cd% == %cd% ( goto :{label123} ) else ( goto :{labeled} )",
                f";if 0 equ 0 ( goto :{labeled} ) else ( goto :{label123} )",
                f";if exist C:\Windows\System3 ( goto :{label123} ) else ( goto :{labeled} )",
                f";if %cd% == %cd% ( goto :{labeled} ) else ( goto :{label123} )",
                f";if chcp leq 1 ( goto :{label123} ) else ( goto :{labeled} )",
                f";if not defined KDOT ( goto :EOF ) else ( goto :{labeled} )",
            ]
        randomed = random.choice(examples)
        obfuscated = self.obf_oneline(randomed)
        self.rep_num += 1
        return obfuscated

    @staticmethod
    def random_semi_and_comma(string):
        symbols = [";", ",", " ", "     "]
        random_symbols = "".join(random.choice(symbols) for _ in range(randint(3, 7)))
        new_string = random_symbols + string + random_symbols
        return new_string

    def random_inserts(self, main_list):
        listes = [
            ";::Made by K.Dot and Godfather\n",
            ";::Good luck deobfuscating\n",
            ";::Made with Somalifuscator\n",
        ]
        for i in range(len(main_list)):
            if i == 0:
                continue
            else:
                random_int = randint(1, 10)
                if random_int == 10:
                    list_choice = random.choice(listes)
                    main_list.insert(i, [list_choice])

        return main_list

    def bad_labels(self, main_list):
        main_dict = self.dict_thing.copy()
        new_list = []
        bad_insert = "​"
        for item in main_dict.values():
            strung = str(item[1])
            strung = ";:" + bad_insert + strung
            new_list.append(strung)
        for array in main_list:
            random_chance = randint(1, 5)
            if random_chance == 5:
                random_label = random.choice(new_list)
                array.insert(0, random_label)
        return main_list

    def first_line_echo_check(self):
        # I hate people who echo :angryface:
        self.checked123 = True
        self.debug = False
        if self.debug:
            if self.checked123 == True:
                command = (
                    r'echo @echo off > close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( (goto) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat'
                    + "\n"
                )
                self.checked123 = not self.checked123
                return command
            else:
                command = (
                    r'echo @echo off >> close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( (goto) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat'
                    + "\n"
                )
                return command
        else:
            if self.checked123 == True:
                command = (
                    """IF /I %0 NEQ "%~dpnx0" (del close.bat & exit)\necho @echo off > close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( (goto) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat"""
                    + "\n"
                )
                self.checked123 = not self.checked123
                return command
            else:
                command = (
                    """IF /I %0 NEQ "%~dpnx0" (del close.bat & exit)\necho @echo off >> close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( (goto) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat"""
                    + "\n"
                )
                return command

    def anti_check_error(self, code):
        strung = ">nul 2>&1 && exit >nul 2>&1 || cls \n@%nobruh%e%nobruh%c%nobruh%h%nobruh%o o%nobruh%f%nobruh%f%nobruh%\n"
        code.insert(0, strung)

        # There is a 99% chance I could have just used .encode() but im just lazy like that if u gotta problem wit it make a pr

        with open("placeholder.bat", "w", encoding="utf-8") as f:
            f.writelines(code)
        with open("placeholder.bat", "rb") as f:
            code = f.read()

        os.remove("placeholder.bat")

        out_hex = []

        # lowkey overkill lmao
        out_hex.extend(["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE"])

        out_hex.extend(["{:02X}".format(b) for b in code])

        return out_hex

    def embed(self):
        starting_code_normal = """<# :validbatch
@echo off
setlocal
cd /d "%~dp0"

echo K.Dot up

powershell.exe -ep Bypass -Command "IEX $([System.IO.File]::ReadAllText('%~f0'))"
goto :eof
#>"""
        starting_code_to_obf = """@echo off
setlocal
cd /d "{%~dp0}"

echo K.Dot up

powershell -ep Bypass -Command "IEX $([System.IO.File]::ReadAllText('{%~f0}'))"
goto :eof
"""
        ps1_file_location = Write.Input(
            "Enter the location of the ps1 file: ", Colors.green, interval=0.05
        )
        try:
            with open(ps1_file_location, "r", encoding="utf-8") as f:
                data = f.readlines()
        except FileNotFoundError:
            print("File not found!")
            time.sleep(3)
            Main()
        obfuscate = Write.Input(
            "Would you like to obfuscate the batch code? (y/n): ",
            Colors.green,
            interval=0.05,
        )
        if obfuscate.lower() == "y":
            with open("place_holder.bat", "w", encoding="utf-8") as f:
                f.write(starting_code_to_obf)
                self.file = "place_holder.bat"
            self.ultimate()
            os.remove("place_holder.bat")
            os.rename("place_holder.bat.ultimate.bat", "embed.bat")
            with open("embed.bat", "r+", encoding="utf-8") as f:
                data2 = f.readlines()
                data2_size = len(data2)
                data2.insert(0, "<# :validkdot\n")
                data2.insert(data2_size + 1, "#>\n")
                data2 += data
            with open("embed.bat", "w+", encoding="utf-8") as f:
                f.writelines(data2)
        else:
            # I can FASHO make this a lot cleaner and better but im too lazy rn (split string into list instead of reading it from file :skull:)
            with open("embed.bat", "w", encoding="utf-8") as f:
                f.write(starting_code_normal)
            with open("embed.bat", "r+", encoding="utf-8") as f:
                data2 = f.readlines()
            with open("embed.bat", "w", encoding="utf-8") as f:
                data2_size = len(data2)
                data2.insert(data2_size, "\n")
                data2 += data
                f.writelines(data2)

    def level4(self):
        # Level 4 as promised. (I lowkey skidded it from someone else but i cant remember who :skull:) W mans tho ong
        # Also I can remake this instead of using JScript, etc
        batch_code = """@if (@CodeSection == @Batch) @then


@echo off
setlocal DisableDelayedExpansion

if "%~1" equ "" echo Usage: Obfuscate filename.bat & goto :EOF
if not exist "%~1" echo File not found: "%~1" & goto :EOF

set "at=@"
set "pass=%random%"
(
    echo %at%if (@Pass == @X%pass%^) @begin
    echo    @echo off
    echo    CScript //nologo //E:JScript.Encode "%%~F0" ^> %pass%.bat
    echo    call %pass%
    echo    del /f /q %pass%.bat
    echo    exit /B
    echo %at%end 
    echo //**Start Encode**
    echo var a = new Array(^);

    set "i=0"
    for /F "usebackq delims=" %%a in ("%~1") do (
        set /A i+=1
        set "line=%%a"
        setlocal EnableDelayedExpansion
        echo a[!i!] = '!line:'=\x27!';
        endlocal
    )

    setlocal EnableDelayedExpansion
    echo for ( var i=1; i^<=!i!; ++i ^) WScript.Stdout.WriteLine(a[i]^);
) > "%~N1.tmp"

CScript //nologo //E:JScript "%~F0" "%~N1.tmp"
::rename "%~N1.tmp" "%~N1.bat"
::del "%~N1.tmp"
rename "%~N1.tmp" "%~N1.encoded.bat"
goto :EOF


@end

//Made by some guy on stack overflow (I can't find the post anymore + I delete the old comments I had :sob:)
//I had to edit it a lil bit to make it work again. (It didn't work at all for me before)

var fileToEncode = WScript.Arguments(0);

var oFSO = WScript.CreateObject("Scripting.FileSystemObject");
var oFile = oFSO.GetFile(fileToEncode);
var oStream = oFile.OpenAsTextStream(1);
var sSourceFile = oStream.ReadAll();
oStream.Close();

var oEncoder = WScript.CreateObject("Scripting.Encoder");
var sDest = oEncoder.EncodeScriptFile(".js", sSourceFile, 0, "")

var edited_name = fileToEncode.replace(".bat", ".encoded.bat");

var oStream = oFSO.OpenTextFile(fileToEncode, 2, true);
oStream.Write(sDest);
oStream.Close();"""
        with open("level4.bat", "w") as f:
            f.writelines(batch_code)
        os.system("level4.bat " + self.file)
        file_name = self.file.replace(".bat", ".encoded.bat")
        os.rename(f"{file_name}", f"{self.file}.level4.bat")
        os.remove("level4.bat")

    def level5(self):
        batch_code = r"""@echo off
setlocal disableDelayedExpansion
if /i "%~1" equ "/m" set "/m=/m" & shift /1
set "in=%~1"
if not defined in echo Error: Missing inputFile>&2&exit /b
set "out=%~2"
if not defined out set "out=%~dpn1_obfuscated%~x1"
set "find={[:<][^}]*}|^[^:\r\n]?[ \t=,;\xFF]*:[^ \t:\r\n+]*[ \t:\r\n+]?|%%%%|%%\*|%%(?:~[fdpnxsatz]*(?:\$[^:\r\n]+:)?)?[0-9]|%%[^%%\r\n]+%%|%%@[\x20-\x24\x26-\x7E]"
set "repl=$txt=$0@$txt='%%'+String.fromCharCode($0.charCodeAt(0)+129)+'%%'"

setlocal enableDelayedExpansion
set "str1="
set "x=x"
for %%A in (2 3 4 5 6 7) do @for %%B in (0 1 2 3 4 5 6 7 8 9 A B C D E F) do set "str1=!str1!\x%%A%%B"
set "str1=%str1:~0,-4%"
set "str1=%str1:\x22=%\x22"
set "str1=%str1:\x24\x25=DDDD%"
call jrepl x str1 /m /x /v /s x /rtn lo
set "lo=!lo:DDDD=$!"

set "str2="
for %%A in (A B C D E F) do @for %%B in (0 1 2 3 4 5 6 7 8 9 A B C D E F) do set "str2=!str2!\x%%A%%B"
set "str2=%str2:~4%"
set "str2=%str2:\xA3=%\xA3"
set "str2=%str2:\xA6=%"
call jrepl x str2 /m /x /v /s x /rtn hi
call jrepl "" "%%%%=%%%%" /m /x /s hi /rtn hi2

call :write <"!in!" >"!out!"
exit /b

:write
echo @echo off^&(if defined @lo@ goto !hi:~0,1!)^&setlocal disableDelayedExpansion^&for /f "delims=:. tokens=2" %%%%A in ('chcp') do set "@chcp@=chcp %%%%A>nul"^&chcp 708^>nul^&set ^^^^"@args@=%%*"
echo set "@lo@=!lo!"
echo set "@hi@=!hi2!"
echo (setlocal enableDelayedExpansion^&for /l %%%%N in (0 1 93) do set "^!@hi@:~%%%%N,1^!=^!@lo@:~%%%%N,1^!")^&cmd /c ^^^^^""%%~f0" ^^!@args@^^!"
echo %%@chcp@%%^&exit /b
echo :!hi:~0,1!
jrepl "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"^
        "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"^
        %/m% /t "" /p "{[^:}][^}]*}" | jrepl find repl %/m% /t @ /v /x /jq
exit /b """
        with open("level5.bat", "w") as f:
            f.write(batch_code)
        r = requests.get(
            "https://www.dostips.com/forum/download/file.php?id=605", timeout=10
        )
        with open("jrepl.zip", "wb") as f:
            f.write(r.content)
        with ZipFile("jrepl.zip", "r") as zipObj:
            zipObj.extractall()
        os.remove("jrepl.zip")
        os.system("level5.bat " + self.file)
        os.remove("level5.bat")
        os.remove("JREPL.bat")
        file = self.file.replace(".bat", "_obfuscated.bat")
        os.rename(f"{file}", f"{self.file}.level5.bat")

    def pogdog(self):
        raise OverflowError("Pogdog is not implemented yet")

    def bat2exe(self):
        code = r"""[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=0
HideExtractAnimation=1
UseLongFileName=1
InsideCompressed=0
CAB_FixedSize=0
CAB_ResvCodeSigning=0
RebootMode=N
InstallPrompt=%InstallPrompt%
DisplayLicense=%DisplayLicense%
FinishMessage=%FinishMessage%
TargetName=%TargetName%
FriendlyName=%FriendlyName%
AppLaunched=%AppLaunched%
PostInstallCmd=%PostInstallCmd%
AdminQuietInstCmd=%AdminQuietInstCmd%
UserQuietInstCmd=%UserQuietInstCmd%
SourceFiles=SourceFiles

[Strings]
InstallPrompt=
DisplayLicense=
FinishMessage=
FriendlyName=-
PostInstallCmd=<None>
AdminQuietInstCmd=
"""
        current_dir = os.getcwd()
        bat_file_name = os.path.basename(self.file)
        exe_name = bat_file_name[:-4] + ".exe"

        app_launched = "AppLaunched=cmd /c " + '"' + bat_file_name + '"'
        target = f"TargetName={exe_name}"
        file_0 = f"FILE0={bat_file_name}"
        source_files = f"[SourceFiles]\nSourceFiles0={current_dir}"
        extra = f"[SourceFiles0]\n%FILE0%="

        to_write = [app_launched, target, file_0, source_files, extra]
        with open("setup.sed", "a+") as f:
            f.write(code)
            for item in to_write:
                f.write(item + "\n")
        os.system("iexpress /n /q /m setup.sed")
        os.remove("setup.sed")
        print(f"Exe file saved as {exe_name}")

    def bat2exe2(self):
        warning = Write.Input(
            "WARNING: This method requires you to download a exe file from the github repo and run it. Are you ok with this? (y/n): ",
            Colors.green,
            interval=0.05,
        )
        if warning.lower() == "n":
            time.sleep(3)
            Main()
        else:
            r = requests.get(
                "https://github.com/KDot227/Somalifuscator/releases/download/Bat2Exe_Method1/Bat2Exe.exe"
            )
            with open("Bat2Exe.exe", "wb") as f:
                f.write(r.content)
            os.system("start Bat2Exe.exe")
            time.sleep(3)

    def oneline(self):
        batch_code = """
@if (@CodeSection == @Batch) @then


@echo off
setlocal DisableDelayedExpansion

if "%~1" equ "" echo Usage: Obfuscate filename.bat & goto :EOF
if not exist "%~1" echo File not found: "%~1" & goto :EOF

set "pass=%random%"
(
    echo /* @echo off ^& CScript //nologo //E:JScript.Encode "%%~F0" ^> %pass%.bat ^& call %pass% ^& del /f /q %pass%.bat ^& exit /B */ //**Start Encode**
    echo var a = new Array(^);

    set "i=0"
    for /F "usebackq delims=" %%a in ("%~1") do (
        set /A i+=1
        set "line=%%a"
        setlocal EnableDelayedExpansion
        echo a[!i!] = '!line:'=\x27!';
        endlocal
    )

    setlocal EnableDelayedExpansion
    echo for ( var i=1; i^<=!i!; ++i ^) WScript.Stdout.WriteLine(a[i]^);
) > "%~N1.tmp"

CScript //nologo //E:JScript "%~F0" "%~N1.tmp"
::rename "%~N1.tmp" "%~N1.bat"
::del "%~N1.tmp"
rename "%~N1.tmp" "%~N1.encoded.bat"
goto :EOF


@end

//Made by some guy on stack overflow (I can't find the post anymore + I delete the old comments I had :sob:)
//I had to edit it a lil bit to make it work again. (It didn't work at all for me before)

var fileToEncode = WScript.Arguments(0);

var oFSO = WScript.CreateObject("Scripting.FileSystemObject");
var oFile = oFSO.GetFile(fileToEncode);
var oStream = oFile.OpenAsTextStream(1);
var sSourceFile = oStream.ReadAll();
oStream.Close();

var oEncoder = WScript.CreateObject("Scripting.Encoder");
var sDest = oEncoder.EncodeScriptFile(".js", sSourceFile, 0, "")

var edited_name = fileToEncode.replace(".bat", ".encoded.bat");

var oStream = oFSO.OpenTextFile(fileToEncode, 2, true);
oStream.Write(sDest);
oStream.Close();
        """
        with open("oneline.bat", "w") as f:
            f.writelines(batch_code)
        os.system("oneline.bat " + self.file)
        file_name = self.file.replace(".bat", ".encoded.bat")
        os.rename(f"{file_name}", f"{self.file}.oneline.bat")
        os.remove("oneline.bat")


if __name__ == "__main__":
    AutoUpdate()
    Main()
    print("Done!")
    more = Write.Input(
        "Do you want to obfuscate another file? (y/n): ",
        Colors.green,
        interval=0.05,
    )
    if more.lower() == "y":
        os.system("cls")
        Main()
    else:
        time.sleep(1)
        os._exit(0)
