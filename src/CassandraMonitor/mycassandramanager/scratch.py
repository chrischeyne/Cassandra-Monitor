proc = \
            subprocess.Popen(cmd,bufsize=0,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        poll_seconds = .250
        deadline = time.time()+timeout
        while time.time()<deadline and proc.poll()==None:
            time.sleep(poll_seconds)

        if proc.poll() == None:
            if float(sys.version[:3]) >= 2.6:
                proc.terminate()
            raise Timeout()

        stdout,stderr = proc.communicate()


