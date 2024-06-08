import argparse
import os

def c2_install(c2,place):
  print(f"Installing " + c2 + " in " + place)
  os.system("ansible-playbook C2s/CobaltStrike/cs-install.yml -i ./local_host")

def relay_local(relay,place):
  os.system("ansible-playbook C2s/CobaltStrike/cs-install.yml -i ./local_host")

def delete():
  print("RFS Delete software and configuration---")

def main():
  base = argparse.ArgumentParser(
                    prog='Red Labs',
                    description='Red Labs Cloud installer',
                    epilog='Martian Defense Team')
  
  base.add_argument("-i", "--install",  action='store_true',required=False, help="Configure the Labs")
  base.add_argument("-c", "--config", dest="config_file", required=False, help="Configure the Labs")
  base.add_argument("-d", "--delete", required=False, help="Delete the Labs")
  
  deploy = base.add_argument_group('Deploy')
  deploy.add_argument('-l',"--local",  action='store_true',help='Localhost or Network')
  deploy.add_argument('-dg', help='Digital Ocean Cloud')
  deploy.add_argument('-aws', help='AWS Cloud')
  deploy.add_argument('-azr', help='Azure Cloud')

  service = base.add_argument_group('Services')
  service.add_argument('--rl', "--relay",action='store_true',required=False,help='Relay')
  service.add_argument('--c2', "--command-control",help='C2')

  subparsers = base.add_subparsers(
      title="Install", help="Install test"
  )
  add_parser = subparsers.add_parser("local", help="add two numbers a and b")
  add_parser.set_defaults(func=relay_local)

  args = base.parse_args()

  if args.install and args.local =="relay" and args.relay =="socat":
    relay_local()
  elif args.install and args.c2 =="cobalt":
    c2_install('cobalt','local')
  elif args.install == "delete":
    delete()
  else:
    print(f"Invalid action: {args.install}")

if __name__ == "__main__":
  main()