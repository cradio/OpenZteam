# cRadio 2020
import threading
import time
import io  # because of charmap errors


class DB:
    cntDeleted = 0
    cntLines = 0
    cntPublic = 0
    cntChecked = 0
    cntPrivateMYR = 0
    cntPrivateZabugor = 0
    percentPrivate = 0
    MYRDomains = ["ru", "kz", "ua", "by"]
    DB = []

    def __init__(self, dbPath):
        self.dbPath = dbPath

    def readDBThread(self):
        with io.open(self.dbPath, "r", encoding="utf-8") as dbFile:
            for line in dbFile:
                xline = line.replace(';', ':').replace(" ", "").replace("\t", "").replace("\n", "")
                if line == "" or xline == "":
                    continue
                self.cntLines += 1
                if (xline[:1].isalpha() or xline[:1].isnumeric() or xline[:1].startswith("_")) and (":" in xline) and (
                        "@" in xline):
                    self.DB.append(xline)
                else:
                    self.cntDeleted += 1
                    # print(f"----BAD----\t{xline}")

    def readDB(self):
        DBThread = threading.Thread(target=self.readDBThread)
        DBThread.start()
        awaittext = "Reading DB"
        while threading.active_count() > 1:
            for dot in range(4):
                print(
                    f"\r[Bad: {self.cntDeleted} ({round((100 * self.cntDeleted / (1 if self.cntLines == 0 else self.cntLines)), 2)}%)| Total: {self.cntLines}] " + awaittext + "." * dot,
                    end=" " * 3)
                time.sleep(.3)
        print(f"\n[DB] Done. Loaded {self.cntLines - self.cntDeleted} lines")

    def writeDB(self, path):
        with io.open(path, "w", encoding="utf-8") as dbFile:
            dbFile.write(''.join(line + '\n' for line in self.DB))
