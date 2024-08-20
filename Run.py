try:
    import requests, json, sys, time, os, urllib.parse
    from rich.console import Console
    from rich.panel import Panel
    from rich import print as printf
    from requests.exceptions import RequestException
except (ModuleNotFoundError) as e:
    __import__("sys").exit(f"[Error] : {str(e).capitalize()}!")

TOKEN = {
    "KEY": None,
}

class MAIN:
    def __init__(self) -> None:
        pass

    def MISSION(self, token):
        with requests.Session() as session:
            session.headers.update(
                {
                    "Accept-Language": "id,id-ID;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Referer": "https://move.sowscharity.top/",
                    "Authorization": "Bearer {}".format(token),
                    "Origin": "https://move.sowscharity.top",
                    "Content-Type": "application/json",
                    "Host": "move.sowscharity.top",
                    "Lang": "en",
                    "Accept": "*/*",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Infinix X6831 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.103 Mobile Safari/537.36",
                }
            )
            data = json.dumps({"level": "0", "page": 1})
            response = session.post(
                "https://move.sowscharity.top/api/sd/index", data=data
            )
            if '"id":' in str(response.text) and '"data":[' in str(
                response.text
            ):  # IN ORDER TO AVOID BEING SUSPECTED, COMPLETE THE MISSIONS ONE BY ONE!
                self.TITLE = json.loads(response.text)["data"]["data"][0]["good_title"]
                self.ID = json.loads(response.text)["data"]["data"][0]["id"]
                data = json.dumps({"id": f"{self.ID}"})
                response2 = session.post(
                    "https://move.sowscharity.top/api/sd/create", data=data
                )
                if '"id":' in str(response2.text) and '"data":' in str(response2.text):
                    self.ID_MISI = json.loads(response2.text)["data"]["id"]
                    for SLEEP in range(15, 0, -1):
                        time.sleep(1.0)
                        printf(
                            f"[bold bright_white]   ──>[bold white] WAIT[bold green] {SLEEP}[bold white] SECONDS!            ",
                            end="\r",
                        )
                    data = json.dumps({"id": f"{self.ID_MISI}"})
                    response3 = session.post(
                        "https://move.sowscharity.top/api/sd/confirm", data=data
                    )
                    if "Successful operation" in str(response3.text):
                        printf(
                            Panel(
                                f"""[bold white]Status :[italic green] Your mission has been successful...[/]
[bold white]ID :[bold yellow] {self.ID_MISI}
[bold white]Title :[bold red] {self.TITLE}""",
                                style="bold bright_white",
                                width=59,
                                title="> [Sukses] <",
                            )
                        )
                        return "SUKSES"
                    else:
                        printf(
                            Panel(
                                f"""[bold white]Status :[italic red] Failed to complete this mission![/]
[bold white]ID :[bold yellow] {self.ID_MISI}
[bold white]Title :[bold green] {self.TITLE}""",
                                style="bold bright_white",
                                width=59,
                                title="> [Gagal] <",
                            )
                        )
                        return "GAGAL"
                elif "please come back tomorrow" in str(response2.text):
                    printf(
                        f"[bold bright_white]   ──>[bold red] TODAY'S MISSION IS COMPLETED!           ",
                        end="\r",
                    )
                    time.sleep(5.5)
                    return "FINISHED"
                elif "You have pending orders" in str(response2.text):
                    printf(
                        f"[bold bright_white]   ──>[bold red] YOU HAVE 1 PENDING MISSION!             ",
                        end="\r",
                    )
                    time.sleep(5.5)
                    return "PENDING"
                else:
                    printf(
                        f"[bold bright_white]   ──>[bold yellow] ERROR WHILE TAKING MISSION LIST!     ",
                        end="\r",
                    )
                    time.sleep(5.5)
                    return "ERROR"
            else:
                printf(
                    f"[bold bright_white]   ──>[bold red] ERROR WHILE TAKING MISSION LIST!     ",
                    end="\r",
                )
                time.sleep(5.5)
                return "ERROR"

    def LOGIN(self):
        try:
            os.system("cls" if os.name == "nt" else "clear")
            printf(
                Panel(
                    """[bold red]     ______       _                 _             \n    / _____)     | |               (_)  _         \n   ( (____   ____| |__  _____  ____ _ _| |_ _   _ \n    \____ \ / ___)  _ \(____ |/ ___) (_   _) | | |\n    _____) | (___| | | / ___ | |   | | | |_| |_| |\n[bold white]   (______/ \____)_| |_\_____|_|   |_|  \__)\__  |\n                                           (____/ \n       [underline green]Sowscharity Mission Bypass - by Rozhak""",
                    style="bold bright_white",
                    width=59,
                )
            )

            printf(
                Panel(
                    f"[bold white]You must fill in the username and password of the registered account, use `[bold red]:[bold white]` as a\nseparator and `[bold red]#[bold white]` to fill in multiple accounts!",
                    style="bold bright_white",
                    width=59,
                    title="> [Login Diperlukan] <",
                    subtitle="╭──────",
                    subtitle_align="left",
                )
            )
            self.AKUN = Console().input("[bold bright_white]   ╰─> ")
            if ":" in self.AKUN:
                TASK = []
                printf(
                    Panel(
                        f"[bold white]Working on all missions, please wait and if there is an error check the error log, you can use[bold red] CTRL +\nZ[bold white] to stop and make sure your connection is stable!",
                        style="bold bright_white",
                        width=59,
                        title="> [Catatan] <",
                    )
                )
                for LIST in self.AKUN.split("#"):
                    if ":" in LIST:
                        self.USERNAME = LIST.split(":")[0]
                        self.PASSWORD = LIST.split(":")[1]
                        self.STATUS = self.AUTHORIZATION(self.USERNAME, self.PASSWORD)
                        if self.STATUS == True:
                            TASK.append(f'{TOKEN["KEY"]}')
                            ERROR, PERCOBAAN = 0, 0
                            while True:
                                try:
                                    if int(ERROR) <= 5:
                                        self.RESPONSE = self.MISSION(f'{TOKEN["KEY"]}')
                                        if (
                                            self.RESPONSE == "PENDING"
                                            or self.RESPONSE == "FINISHED"
                                        ):
                                            break
                                        elif self.RESPONSE == "ERROR":
                                            ERROR += 1
                                            continue
                                        else:
                                            if int(PERCOBAAN) <= 5:
                                                PERCOBAAN += 1
                                                continue
                                            else:
                                                break
                                    else:
                                        break
                                except (RequestException):
                                    printf(
                                        f"[bold bright_white]   ──>[bold red] YOUR CONNECTION HAS BEEN DISCONNECTED!     ",
                                        end="\r",
                                    )
                                    time.sleep(8.5)
                                    continue
                            printf(
                                f"[bold bright_white]   ──>[bold green] @{str(self.USERNAME).upper()} MISSION COMPLETED!     ",
                                end="\r",
                            )
                            time.sleep(4.5)
                            continue
                        else:
                            continue
                    else:
                        continue
                if len(TASK) == 0:
                    printf(
                        Panel(
                            f"[bold red]None of the accounts you have filled in can be logged in, please try again!",
                            style="bold bright_white",
                            width=59,
                            title="> [Error] <",
                        )
                    )
                    sys.exit()
                else:
                    printf(
                        Panel(
                            f"[bold white]We have successfully completed all missions, come back tomorrow after[bold red] 24 hours[bold white] to complete more missions!",
                            style="bold bright_white",
                            width=59,
                            title="> [Selesai] <",
                        )
                    )
                    Console().input("[bold white][[bold green]Selesai[bold white]]")
                    sys.exit()
            else:
                printf(
                    Panel(
                        f"[bold red]You entered the wrong separator between username and password, please try again!",
                        style="bold bright_white",
                        width=59,
                        title="> [Pemisah Salah] <",
                    )
                )
                sys.exit()
        except (Exception) as e:
            printf(
                Panel(
                    f"[bold red]{str(e).capitalize()}!",
                    style="bold bright_white",
                    width=59,
                    title="> [Error] <",
                )
            )
            sys.exit()

    def AUTHORIZATION(self, username, password):
        global TOKEN
        with requests.Session() as session:
            data = json.dumps(
                {
                    "password": f"{password}",
                    "phone": f"{username}",
                }
            )
            session.headers.update(
                {
                    "Referer": "https://move.sowscharity.top/",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Connection": "keep-alive",
                    "Content-Length": "{}".format(len(urllib.parse.quote(str(data)))),
                    "Content-Type": "application/json",
                    "Host": "move.sowscharity.top",
                    "Lang": "en",
                    "Origin": "https://move.sowscharity.top",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "Accept": "*/*",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                }
            )
            response = session.post(
                "https://move.sowscharity.top/api/user/login", data=data
            )
            if '"token":' in str(response.text):
                self.TOKEN = json.loads(response.text)["data"]["token"]
                TOKEN.update({"KEY": f"{self.TOKEN}"})
                return True
            else:
                printf(
                    f"[bold bright_white]   ──>[bold red] TOKEN FROM @{username} NOT FOUND!     ",
                    end="\r",
                )
                time.sleep(5.5)
                TOKEN.update({"KEY": None})
                return False

if __name__ == "__main__":
    try:
        os.system("git pull")
        MAIN().LOGIN()
    except (KeyboardInterrupt):
        sys.exit()