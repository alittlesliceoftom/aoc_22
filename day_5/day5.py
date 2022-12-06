
STACK_COUNT = 9

def get_initial_config():
  # Open the input file
  with open("start.txt") as f:
    # Read the lines of the file
      lines = f.readlines()

  #top to bottom so reverse
  lines.reverse()
  # Create a list of stacks, where each stack is represented as a list of crates
  stacks = [[] for _ in range(STACK_COUNT)]

  # Parse the input file
  for line in lines:
    # Split the line into a list of crates
      crates = [ line[1+i*4:2+i*4] for i in range(STACK_COUNT)]

    # print(crates)
    # Add each crate to the corresponding stack
      for i, crate in enumerate(crates):
          if crate != ' ':
              stacks[i].append(crate)
  return stacks

def get_moves():
  """read in moves file"""
  with open("moves.txt") as f:
    # Read the lines of the file
    moves = f.readlines()
  return moves

def apply_moves(stacks,moves):
  """Function which applies moves given a stack"""
  move_split = moves[0].split()
  #parse first move
  num, frm, to = list(map(int,move_split[1::2]))
  frm, to = frm-1, to-1
  print(moves[0])
  # apply
  for _ in range(num):
    print(f'moving {stacks[frm][-1]} from {stacks[frm]} to {stacks[to]}')
    stacks[to].append(stacks[frm].pop(-1))
  if len(moves) > 1:
    return apply_moves(stacks, moves[1:])
  else:
    return stacks

if __name__ == "__main__":
  stacks = get_initial_config()
  print(f"init config, {stacks}")
  moves = get_moves()
  final_stacks = apply_moves(stacks,moves)
  # Print the top crate on each stack
  for stack in final_stacks:
      print(stack[-1])

