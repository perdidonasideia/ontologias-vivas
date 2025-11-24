import json
import argparse
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from generator.build import generate

def push_to_sheet(sheet_id, range_name, n, credentials_json):
    creds = Credentials.from_service_account_info(credentials_json)
    service = build("sheets", "v4", credentials=creds)
    values = []

    topics = generate(n)
    for t in topics:
        values.append([
            t["id"],
            t["título"],
            t["descrição"],
            t["pergunta_central"],
            "; ".join(t["subperguntas"]),
            t["escopo"],
            "; ".join(t["métodos_sugeridos"]),
            "; ".join(t["palavras_chave"]),
            "; ".join(t["implicacoes_eticas"]),
            t["provocacao_pratica"],
            t["nivel"]
        ])

    body = {"values": values}

    service.spreadsheets().values().append(
        spreadsheetId=sheet_id,
        range=range_name,
        valueInputOption="RAW",
        body=body
    ).execute()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sheet_id")
    parser.add_argument("--range", default="A1")
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--creds", type=str, required=True)
    args = parser.parse_args()

    creds_json = json.loads(args.creds)
    push_to_sheet(args.sheet_id, args.range, args.count, creds_json)
