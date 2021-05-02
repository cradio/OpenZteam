from libs import myrz_api
from libs import services
from libs import db
import argparse


def banner():
    print(f"""
     ██████╗ ██████╗ ███████╗███╗   ██╗███████╗████████╗███████╗ █████╗ ███╗   ███╗
    ██╔═══██╗██╔══██╗██╔════╝████╗  ██║╚══███╔╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
    ██║   ██║██████╔╝█████╗  ██╔██╗ ██║  ███╔╝    ██║   █████╗  ███████║██╔████╔██║
    ██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║ ███╔╝     ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
    ╚██████╔╝██║     ███████╗██║ ╚████║███████╗   ██║   ███████╗██║  ██║██║ ╚═╝ ██║
     ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
     """)


def main(args):
    if args.guid:
        exit("Token: " + services.calculateToken(args.guid))
    elif args.gen:
        exit("Generated token: " + services.getFakeToken())
    elif args.clean:
        if not args.db_path:
            exit("[E] No DB selected (-db)")
        xdb = db.DB(args.db_path)
        print("[i] Cleaning DB")
        xdb.readDB()
        xdb.writeDB(args.db_path + "_clean")
    else:
        if not args.token:
            exit("[E] No Token Specified")
        api = myrz_api.API(args.token)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="OpenZteam is an alternative open-source cli interface for AntiPublic with extra features")
    parser.add_argument("-a", "--api-key", dest="token",
                        help="Activated AntiPublic key. If you don't have one generate it with --api-gen and paste at https://lolz.guru/account/antipublic")
    parser.add_argument("--api-gen", dest="gen", action="store_true", default=False, help="Generate client key")
    parser.add_argument("--api-calc", dest="guid",
                        help="Windows GUID (HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography -> MachineGuid). "
                             "Useful if you have access to victim machine or this value itself and victim uses AntiPublic client")
    parser.add_argument("-db", dest="db_path", help="DB to check")
    parser.add_argument("--clean", dest="clean", action="store_true", default=False, help="Don't process DB. Only remove bad entries and write to [filename]-clean.txt")

    args = parser.parse_args()
    banner()
    main(args)
