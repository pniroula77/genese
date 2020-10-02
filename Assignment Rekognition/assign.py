#Author: Pawan Niroula

import boto3

image = 'image.jpg'

client = boto3.client('rekognition')

with open(image,'rb') as image_test:
    image_byte = image_test.read()


response = client.detect_faces(
    Image={'Bytes':image_byte},
    Attributes=['ALL'])


for face in response['FaceDetails']:

    # Extracting the age of person in picture
    age_low = str(face['AgeRange']['Low'])
    age_high = str(face['AgeRange']['High'])

    # Extracting the gender and confidence of person 
    gender = str(face['Gender']['Value'])
    gender_confidence = str(face['Gender']['Confidence'])

    # Extracting Emotions 
    emotion = str(face['Emotions'][0])
    emotion_confidence = str(face['Emotions'][1])

    #Extracting Beard
    beard_value = str(face['Beard']['Value'])
    beard_confidence = str(face['Beard']['Confidence'])

    #Extracting Mustache
    mustache_value = str(face['Mustache']['Value'])
    mustache_confidence = str(face['Mustache']['Confidence'])

    #Extracting sunglasses
    sunglass_value = str(face['Sunglasses']['Value'])
    sunglass_confidence = str(face['Sunglasses']['Confidence'])

    print('Age Range :', age_low + '-' + age_high)
    print('Gender :',gender + ' Confidence :', gender_confidence )
    print('Feeling :' ,emotion + 'Confidence :',emotion_confidence)
    
    if beard_value == True:
        print('Has Beard with Confidence:',beard_confidence)
    if beard_value != True:
        print('No Beard with Confidence:' ,beard_confidence)
    
    if mustache_value == True:
        print('Has Mustache with Confidence:',mustache_confidence)
    
    if mustache_value != True:
        print('No Mustache with Confidence:' ,mustache_confidence)
        
    if sunglass_value == True:
        print('Has Sunglasses with Confidence:', sunglass_confidence)
    if sunglass_value != True:
        print('No Sunglasses with Confidence:', sunglass_confidence)


