import subprocess
import sys
from datetime import datetime

# Mensagem de commit padrão ou personalizada
commit_message = (
    sys.argv[1] if len(sys.argv) > 1 else f"Auto-commit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)

def run_git_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Erro ao executar {' '.join(cmd)}:\n{result.stderr}")
        sys.exit(1)
    else:
        print(result.stdout)

# Adiciona todos os arquivos alterados
run_git_command("git add .")
# Faz o commit
run_git_command(f'git commit -m "{commit_message}"')
# Dá push para o repositório remoto
run_git_command("git push")
