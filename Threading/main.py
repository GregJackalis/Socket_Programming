import threading
import time  # we will the .sleep() method to create some downtime

done = False

def worker(text):
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(f"{text}: {counter}\n")


threading.Thread(target=worker, daemon=True, args=("ABC",)).start()
threading.Thread(target=worker, daemon=True, args=("XYZ",)).start()

# OR, if we want for the threads to finish first running and then continue with the code below (the input command), we can do this
t1 = threading.Thread(target=worker, daemon=True, args=("ABC",))
t2 = threading.Thread(target=worker, daemon=True, args=("XYZ",))

t1.join()  # this method is used "to tell the program" to pause and wait for that specific (t1 in this case) thread to finishing being
           # executed, before continuing with the subsequenct code (the code below)
t2.join()



input("Press enter to quit")  # so if we're using the .join() thread metho, then this text right here won't appear in the console until
                              # the thread that's running in the code above is done
done = True