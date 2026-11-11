import argparse
import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tarefas.json")


def carregar_tarefas():
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def salvar_tarefas(tarefas):
    DATA_FILE.write_text(
        json.dumps(tarefas, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def adicionar_tarefa(titulo, prioridade):
    tarefas = carregar_tarefas()
    tarefa = {
        "id": max((t["id"] for t in tarefas), default=0) + 1,
        "titulo": titulo,
        "prioridade": prioridade,
        "concluida": False,
        "criada_em": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print(f"Tarefa #{tarefa['id']} adicionada com sucesso.")


def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada. Use: python main.py adicionar \"Minha tarefa\"")
        return

    print("\n=== MINHAS TAREFAS ===")
    for tarefa in tarefas:
        estado = "✓" if tarefa["concluida"] else " "
        print(
            f"[{estado}] #{tarefa['id']} | {tarefa['titulo']} "
            f"| Prioridade: {tarefa['prioridade']} | Criada em: {tarefa['criada_em']}"
        )
    print()


def concluir_tarefa(tarefa_id):
    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["concluida"] = True
            salvar_tarefas(tarefas)
            print(f"Tarefa #{tarefa_id} marcada como concluída.")
            return
    print(f"Tarefa #{tarefa_id} não encontrada.")


def remover_tarefa(tarefa_id):
    tarefas = carregar_tarefas()
    novas_tarefas = [t for t in tarefas if t["id"] != tarefa_id]
    if len(novas_tarefas) == len(tarefas):
        print(f"Tarefa #{tarefa_id} não encontrada.")
        return
    salvar_tarefas(novas_tarefas)
    print(f"Tarefa #{tarefa_id} removida.")


def criar_parser():
    parser = argparse.ArgumentParser(
        description="OrganizaPy — gerenciador simples de tarefas pelo terminal."
    )
    comandos = parser.add_subparsers(dest="comando", required=True)

    adicionar = comandos.add_parser("adicionar", help="Cadastra uma nova tarefa.")
    adicionar.add_argument("titulo", help="Título da tarefa.")
    adicionar.add_argument(
        "--prioridade",
        choices=["baixa", "media", "alta"],
        default="media",
        help="Prioridade da tarefa (padrão: media).",
    )

    comandos.add_parser("listar", help="Mostra todas as tarefas.")

    concluir = comandos.add_parser("concluir", help="Conclui uma tarefa.")
    concluir.add_argument("id", type=int, help="ID da tarefa.")

    remover = comandos.add_parser("remover", help="Remove uma tarefa.")
    remover.add_argument("id", type=int, help="ID da tarefa.")

    return parser


def main():
    args = criar_parser().parse_args()

    if args.comando == "adicionar":
        adicionar_tarefa(args.titulo, args.prioridade)
    elif args.comando == "listar":
        listar_tarefas()
    elif args.comando == "concluir":
        concluir_tarefa(args.id)
    elif args.comando == "remover":
        remover_tarefa(args.id)


if __name__ == "__main__":
    main()
