from enum import Enum
mem = [0] * 256  
acc = 0          
pc = 0           
running = True   

class Instruction(Enum):
    LOAD = 0
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    STORE = 5
    HALT = 6

instr_map = {
    "LOAD": Instruction.LOAD,
    "ADD": Instruction.ADD,
    "SUB": Instruction.SUB,
    "MUL": Instruction.MUL,
    "DIV": Instruction.DIV,
    "STORE": Instruction.STORE,
    "HALT": Instruction.HALT,
}

program = []

def execute(instr: Instruction, addr: int) -> None:
    
    global acc, pc, running

    if instr == Instruction.LOAD:
        acc = mem[addr]
    elif instr == Instruction.ADD:
        acc += mem[addr]
    elif instr == Instruction.SUB:
        acc -= mem[addr]
    elif instr == Instruction.MUL:
        acc *= mem[addr]
    elif instr == Instruction.DIV:
        if mem[addr] != 0:
            acc = int(acc / mem[addr])  
        else:
            print("Error: division por cero")
    elif instr == Instruction.STORE:
        mem[addr] = acc
    elif instr == Instruction.HALT:
        running = False

    pc += 1
    print(f"PC: {pc} | ACC: {acc}")


def show_memory(from_idx: int = 0, to_idx: int = 20) -> None:
    for i in range(from_idx, to_idx + 1):
        print(f"mem[{i}] = {mem[i]}")


def interactive_loop() -> None:
    global pc, running

    print("\nModo interactivo. Escribe comandos como:")
    print("  set <direccion> <valor>")
    print("  instr <nombre> <direccion>")
    print("  run")
    print("  status")
    print("  exit")

    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()  
            break

        if not line:
            continue

        parts = line.split()
        cmd = parts[0]

        if cmd == "set":
            if len(parts) != 3:
                print("Uso: set <direccion> <valor>")
                continue
            try:
                addr = int(parts[1])
                val = int(parts[2])
            except ValueError:
                print("Argumentos invalidos. Usa enteros.")
                continue
            if 0 <= addr < len(mem):
                mem[addr] = val
            else:
                print("Direccion invalida.")

        elif cmd == "instr":
            if len(parts) != 3:
                print("Uso: instr <nombre> <direccion>")
                continue
            name = parts[1]
            try:
                addr = int(parts[2])
            except ValueError:
                print("Direccion invalida. Usa un entero.")
                continue
            if name in instr_map:
                program.append((instr_map[name], addr))
            else:
                print("Instruccion desconocida.")

        elif cmd == "run":
            pc = 0
            running = True
            while running and pc < len(program):
                instr, addr = program[pc]
                execute(instr, addr)

        elif cmd == "status":
            print(f"ACC: {acc} | PC: {pc}")
            show_memory(0, 15)

        elif cmd == "exit":
            break

        else:
            print("Comando no reconocido.")

def main() -> None:
    print("Emulador de procesador interactivo en Python")
    interactive_loop()

if __name__ == "__main__":
    main()
