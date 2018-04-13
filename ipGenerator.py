import pyping,getopt,sys,socket
from progress.spinner import Spinner
from IP import IP

verbose = "0"
desiredIP = 3
output = ""
ipList = []
dnsRev = []
def main(argv):
	global verbose
	global desiredIP
	global output
	if len(argv) == 1 and argv[0] == '--help':
		helpFile = open("help.txt")
		for line in helpFile:
			print line
		sys.exit(2)
	try:
		opts, argv = getopt.getopt(argv, "", ('verbose=', 'desiredIP=', 'output=' ) )	
	except getopt.GetoptError as err:
		print str(err)
		sys.exit(2)
	for opt,arg in opts:
		if opt == '--verbose':
			verbose = arg
		elif opt == '--desiredIP':
                	desiredIP = int(arg)
		elif opt == '--output':
                	output = arg
	searchIP()
	if output != "":
		saveListOfIP()
	else:
		printListOfIP()
	sys.exit(2)

def searchIP():
	ip = IP()
        count = 0
	global ipList
	if verbose == "0": #No verbosity
		spinner = Spinner('I m Computing...')
        	while (count < desiredIP):
			spinner.next()
			try:
                		r = pyping.ping(ip.generateRandomIP4())
                		if r.ret_code == 0:
					dnsReverse(r.destination)
					ipList.insert(count, r.destination)
	                       		count = count + 1
			except:
				print("")	
	elif verbose == "1": #verbosity
		while (count < desiredIP):
			ipGenerato = ip.generateRandomIP4()
			print "\nGenerated IP4: " + ipGenerato
			print "\nTesting it\n"
			try:
				r = pyping.ping(ipGenerato)
				if r.ret_code == 0:
					print r.destination + " " + "reachable"
					dnsReverse(r.destination)
                                	ipList.insert(count, r.destination)
					count = count + 1
				elif r.ret_code == 1:
					print r.destination + " " + "unreachable"
			except:
				print("")
	return

def dnsReverse(ip):
	global dnsRev
	hostname = ""
	try:
		socketHostInfo = socket.gethostbyaddr(ip)
		hostname = socketHostInfo[0]
	except:
		hostname = "unknown"
	dnsRev.insert(len(dnsRev), hostname)
	return

def saveListOfIP():
	file = open(output, "w+")
        for i in range(len(ipList)):
        	file.write("IP: " + ipList[i]+ " " + "Hostname: "  + dnsRev[i]  + "\n")
	file.close()
	print "\nfile " + output + " generated"
	return

def printListOfIP():
	print("\nComputation Complete")
	for i in range(len(ipList)):
        	print "IP: " + ipList[i]+ " " + "Hostname: "  + dnsRev[i]
	return	

if __name__ == "__main__":
    main(sys.argv[1:])
