import requests
import sys
import cv2 
from twilio.rest import Client 

def msg_send():        
    account_sid = 'ACe044c4864789cd3b61f5fea7b9573cca' 
    auth_token = '0cf6ec8281b2ab97632d648d6d042f5d' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',
                                media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
                                body='Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/',      
                                to='whatsapp:+917598553871' 
                            ) 
    
    print(message.sid)
def cam_trig():
    vid = cv2.VideoCapture(0)
    frame_count=0
    while(True):
            
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        frame_count+=1
        # Display the resulting frame
        cv2.imshow('frame', frame)
        if(not(frame_count%10)):
            cv2.imwrite("frame_count"+str(frame_count/10)+".jpg",frame)
            break
        # if(frame_count>300):
        #     break
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows

    cv2.destroyAllWindows()
    msg_send()


def content_gathering(uri):   #Function to request the required web page html content
        pg = requests.get(uri)

        if pg.status_code == 200:
            contents = pg.content

            dist_val=str(contents).split('p')[1][1:len(str(contents).split('p')[1])-3]
            if(float(dist_val)>50 and float(dist_val)<200):
                cam_trig()
        else:
            print("Can't Retrieve the contente Due to some error")


content_gathering(sys.argv[1])



