from datetime import datetime
import random_responses
def isoweekday():
    pass
def sample_responses(input_text, random_item=True, random_list=True):
    user_message = str(input_text).lower()

    if user_message in ("hey","hello", "hi", "sup","is anyone there?", "hello", "good day", "whats up", "greetings"):
        return "Hey! How's it going?"

    if user_message in ("assist", "help", "i need help", "i want help", ):
        return "I'm here to help you deal with health related concerns. Here's what you can ask me: \n \n" \
               "Type 1 → Health Concerns \n \n" \
               "Type 2 → Binge Eating Disorders \n \n" \
               "Type R → To set a reminder"


    if user_message in ("who are you", "who r you",):
        return "I am CareHealth Bot!"

    if user_message in ("how are you", "how r you", "how are you?","how are you doing?", "how are you doing"):
        return "Thanks for asking, I'm doing ok. A lot is going on in the world today. I hope you're taking care of yourself.!"

    if user_message in ("i have a severe headache","severe headache", "headache", "head", "i have headache", "i have a headache","i'm having a severe headache", "i'm having a headache", "head ache", "I'm having headache"):
        return "Headaches can have causes that aren't due to underlying disease. Examples include lack of sleep, an incorrect eyeglass prescription, stress, loud noise exposure or tight head wear. \n \n" \
               "✔Treatments include:\n \n" \
               "Remedies that may reduce headache pain include aspirin, paracetamol and ibuprofen. Resting in a darkened room may also help. \n \n" \
               "✔Recommended By Experts:\n \n" \
               "➤Practo, India’s no.1 online doctor consultation app, offers complete telemedicine solutions for you and your family’s health and medical needs.\n" \
               "➤24/7 Online Doctor Consultation, Online Medicine Delivery & Family Health Plans. \n \n" \
               "https://www.practo.com/"

    if user_message in ("i have cold","i had cold", "cold", "i am sneezing","sneeze", "i have running nose", "i had running nose","running nose",):
        return "A common viral infection of the nose and throat. In contrast to the flu, a common cold can be c""aused by many different types of viruses. The condition is generally harmless and symptoms usually resolve within two weeks.\n \n" \
               "✔Treatments include:\n \n" \
               "The common cold is a viral infection in your upper respiratory tract. Viruses cannot be treated with antibiotics. In most cases, viruses like the cold just need to run their course. You can treat the symptoms of the infection, but you can’t actually treat the infection itself. Cold treatments generally fall into two main categories: over-the-counter (OTC) medications and home remedies.\n \n" \
               "✔Recommended By Experts:\n \n" \
               "➤Practo, India’s no.1 online doctor consultation app, offers complete telemedicine solutions for you and your family’s health and medical needs.\n" \
               "➤24/7 Online Doctor Consultation, Online Medicine Delivery & Family Health Plans. \n \n" \
               "https://www.practo.com/"

    if user_message in ("I have a chest pain", "I had a chest pain", "I had a chest burn", "I have a chest burn", "chest pain", "chest burn", "I have heaviness","I had heaviness", "heaviness", "breathlessness", "acid reflux", "vomitting",):
        return "Chest pain can have causes that aren't due to underlying disease. Examples include heavy lifting, weight lifting, trauma to the chest or swallowing a large piece of food.\n \n" \
               "✔Treatments include:\n \n" \
               "To prevent heartburn, it's best to avoid lying down for at least two hours after eating. Avoiding fats, chocolate and citrus foods may also help. Antacid medications may ease symptoms immediately. Other medications such as omeprazole and ranitidine take longer to work, but may provide more effective relief if prescribed by a doctor..\n\n" \
               "✔Recommended By Experts:\n \n" \
               "➤Practo, India’s no.1 online doctor consultation app, offers complete telemedicine solutions for you and your family’s health and medical needs.\n" \
               "➤24/7 Online Doctor Consultation, Online Medicine Delivery & Family Health Plans. \n \n" \
               "https://www.practo.com/"

    if user_message in ("date","time",):
        now= datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    # if user_message in ("day","which day of the week is it?",):
    #     now= isoweekday()
    #     day_week = now.strfday()
    #     return str(day_week)

    if user_message in ("good", "great", "nice"):
        return "I'm glad to hear that!"

    if user_message in ("frequent urination", "frequently urinating","increased urination", "thirsty", "increased thirty" ,"hunger", "hungry", "i feel thirsty", "i feel hungry", "i have blurry vision", "blurry vision", "blurred vision", "my vision is blurry", "i am urinating too often"  ):
        return "Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy. Your body breaks down most of the food you eat into sugar (glucose) and releases it into your bloodstream. When your blood sugar goes up, it signals your pancreas to release insulin.\n \n" \
               "There are a few different types of diabetes:\n \n" \
               "Type 1: Type 1 diabetes is an autoimmune disease. The immune system attacks and destroys cells in the pancreas, where insulin is made. It’s unclear what causes this attack.\n \n" \
               "Type 2: Type 2 diabetes occurs when your body becomes resistant to insulin, and sugar builds up in your blood. It’s the most common type—about 90% to 95%Trusted Source of people living with diabetes have type 2.\n \n" \
               "Gestational: Gestational diabetes is high blood sugar during pregnancy. Insulin-blocking hormones produced by the placenta cause this type of diabetes.\n \n" \
               "✔Treatments:\n \n" \
               "Most people with diabetes take insulin using a needle and syringe, insulin pen, or insulin pump. Inhalers and insulin jet injectors are less common ways to take insulin. \n \n" \
               "✔Recommended By Experts:\n \n" \
               "➤Practo, India’s no.1 online doctor consultation app, offers complete telemedicine solutions for you and your family’s health and medical needs.\n" \
               "➤24/7 Online Doctor Consultation, Online Medicine Delivery & Family Health Plans. \n \n" \
               "https://www.practo.com/"

    if user_message in ("thank you", "thanks", "thanks a lot","ok","Bye", "Bye, Thanks", "Thanks!, Bye"):
        return "I'm honoured to serve!"

    if user_message in ("1", "1)", "1.","health related concerns"):
        return "What kind of an episode did you have? Please mention (in words) a specific symptom for an accurate result."

    if user_message in ("R", "r", "reminder", "Reminder"):
        return "To set a reminder, click on the below link: \n\n" \
               "https://t.me/CareHealthReminderbot"

    if user_message in ("excess body fat","body fat", "snoring", "insomnia", "weight gain", "unusual weight gain",):
        return "Obesity occurs when a person's body mass index is 25 or greater. The excessive body fat increases the risk of serious health problems.\n\n" \
               "Binge-eating disorder (BED) and night-eating syndrome (NES) are two forms of disordered eating associated with overweight and obesity. While these disorders also occur in non-obese persons, they seem to be associated with weight gain over time and higher risk of diabetes and other metabolic dysfunction. \n\n" \
               "✔Causes:\n \n" \
               "Obesity is generally caused by eating too much and moving too little. If you consume high amounts of energy, particularly fat and sugars, but do not burn off the energy through exercise and physical activity, much of the surplus energy will be stored by the body as fat.\n\n" \
               "✔Treatments:\n \n" \
               "The mainstay of treatment is lifestyle changes such as diet and exercise.\n\n" \
               "✔Recommended By Experts:\n \n" \
               "➤Practo, India’s no.1 online doctor consultation app, offers complete telemedicine solutions for you and your family’s health and medical needs.\n" \
               "➤24/7 Online Doctor Consultation, Online Medicine Delivery & Family Health Plans. \n \n" \
               "https://www.practo.com/"

    if user_message in ("trouble in walking","unable to walk properly", "trouble in understanding", "trouble in speaking", "trouble in speaking and understanding","trouble in understanding and speaking", "paralysis", "numbness", "numbness of face", "numbness of arm", "numbness of leg","numbness of arms", "numbness of legs","partial paralysis","restricted body movements" ):
        return "An ischemic stroke occurs when the blood supply to part of the brain is interrupted or reduced, preventing brain tissue from getting oxygen and nutrients. Brain cells begin to die in minutes. A stroke is a medical emergency, and prompt treatment is crucial. Early action can reduce brain damage and other complications..\n\n" \
               "Binge-eating disorder (BED) and night-eating syndrome (NES) are two forms of disordered eating associated with overweight and obesity. While these disorders also occur in non-obese persons, they seem to be associated with weight gain over time and higher risk of diabetes and other metabolic dysfunction. \n\n" \
               "✔Causes:\n \n" \
               "The main cause of haemorrhagic stroke is high blood pressure, which can weaken the arteries in the brain and make them more likely to split or rupture.\n\n"\
               "✔Treatments:\n \n" \
               "Early treatment with medication like tPA (clot buster) can minimise brain damage. Other treatments focus on limiting complications and preventing additional strokes.\n\n" \
               "✔Recommended By Experts:\n \n" \
               "➤Practo, India’s no.1 online doctor consultation app, offers complete telemedicine solutions for you and your family’s health and medical needs.\n" \
               "➤24/7 Online Doctor Consultation, Online Medicine Delivery & Family Health Plans. \n \n" \
               "https://www.practo.com/"

    if user_message in ("large waist circumference", "large waist", "big waist", "my waist is growing large", "my waist has grown large", "my waist has become huge", "my waist has become big", "my waist has become large" ):
        return "Metabolic syndrome is a cluster of conditions that occur together, increasing your risk of heart disease, stroke and type 2 diabetes. These conditions include increased blood pressure, high blood sugar, excess body fat around the waist, and abnormal cholesterol or triglyceride levels...\n\n" \
               "✔Causes:\n \n" \
               "Binge-eating disorder (BED) and night-eating syndrome (NES) are two forms of disordered eating associated with overweight and obesity. While these disorders also occur in non-obese persons, they seem to be associated with weight gain over time and higher risk of diabetes and other metabolic dysfunction. \n\n" \
               "✔Treatments:\n \n" \
               "Early treatment with medication like tPA (clot buster) can minimise brain damage. Other treatments focus on limiting complications and preventing additional strokes.\n\n" \
               "✔Recommended By Experts:\n \n" \
               "➤Practo, India’s no.1 online doctor consultation app, offers complete telemedicine solutions for you and your family’s health and medical needs.\n" \
               "➤24/7 Online Doctor Consultation, Online Medicine Delivery & Family Health Plans. \n \n" \
               "https://www.practo.com/"

    if user_message in ("abnormal bumps, unexplained fevers, night sweats, unintentional weight loss" ):
        return "Cancer is a disease in which some of the body’s cells grow uncontrollably and spread to other parts of the body. Cancer can start almost anywhere in the human body, which is made up of trillions of cells...\n\n" \
               "✔Causes:\n \n" \
               "Cancer is caused by genetic changes leading to uncontrolled cell growth and tumor formation. The basic cause of sporadic cancers is DNA damage and genomic instability.  \n\n" \
               "✔Treatments:\n \n" \
               "Treatments may include surgery, chemotherapy and radiation therapy.\n\n" \
               "✔Recommended By Experts:\n \n" \
               "➤Practo, India’s no.1 online doctor consultation app, offers complete telemedicine solutions for you and your family’s health and medical needs.\n" \
               "➤24/7 Online Doctor Consultation, Online Medicine Delivery & Family Health Plans. \n \n" \
               "https://www.practo.com/"

    if user_message in ("pain, body ache, bodyache, body pain, swelling, reduced range of motion, stiffness." ):
        return "Arthritis means inflammation or swelling of one or more joints. It describes more than 100 conditions that affect the joints, tissues around the joint, and other connective tissues. Specific symptoms vary depending on the type of arthritis, but usually include joint pain and stiffness....\n\n" \
               "✔Causes:\n \n" \
               "Arthritis is caused by inflammation of the joints. Osteoarthritis usually comes with age and most often affects the fingers, knees, and hips. Sometimes osteoarthritis follows a joint injury. For example, you might have badly injured your knee when young and develop arthritis in your knee joint years later..  \n\n" \
               "✔Treatments:\n \n" \
               "Medication, physiotherapy or sometimes surgery helps reduce symptoms and improve quality of life.\n\n" \
               "✔Recommended By Experts:\n \n" \
               "➤Practo, India’s no.1 online doctor consultation app, offers complete telemedicine solutions for you and your family’s health and medical needs.\n" \
               "➤24/7 Online Doctor Consultation, Online Medicine Delivery & Family Health Plans. \n \n" \
               "https://www.practo.com/"

    if user_message in ("upper stomach pain, nausea, vomiting, Stomach ache, Stomachache, Stomach ache, Stomachache" ):
        return "Gastritis is a general term for a group of conditions with one thing in common: Inflammation of the lining of the stomach. The inflammation of gastritis is most often the result of infection with the same bacterium that causes most stomach ulcers or the regular use of certain pain relievers.....\n\n" \
               "✔Causes:\n \n" \
               "Gastritis is an inflammation of the stomach lining. Weaknesses or injury to the mucus-lined barrier that protects the stomach wall allows digestive juices to damage and inflame the stomach lining. A number of diseases and conditions can increase the risk of gastritis, including inflammatory conditions, such as Crohn's disease.  \n\n" \
               "Treatments:\n \n" \
               "Treatment depends on the cause. Antibiotics and antacids might help.\n\n" \
               "✔Recommended By Experts:\n \n" \
               "➤Practo, India’s no.1 online doctor consultation app, offers complete telemedicine solutions for you and your family’s health and medical needs.\n" \
               "➤24/7 Online Doctor Consultation, Online Medicine Delivery & Family Health Plans. \n \n" \
               "https://www.practo.com/"

    if user_message in ("2", "2)", "2.", "binge eating disorders"):
        return "Binge Eating Disorder:\n \n" \
               "Frequently consuming unusually large amounts of food in one sitting and feeling that eating behaviour is out of control\n \n" \
               "COMMON CAUSES:\n \n" \
               "Binge eating can have causes that aren't due to underlying disease. Examples include overindulging at holiday celebrations or consuming a lot of calories in preparation for an athletic event such as a marathon.\n \n" \
               "TREATMENTS:\n \n" \
               "The goals for treatment of binge-eating disorder are to reduce eating binges and achieve healthy eating habits. Because binge eating can be so entwined with shame, poor self-image and other negative emotions, treatment may also address these and any other mental health issues, such as depression. By getting help for binge eating, you can learn how to feel more in control of your eating. \n\n\n" \
               "What kind of an episode did you have? Please mention (in words) a specific symptom for an accurate result.\n\n" \

    # return "I am sorry, maybe I didn't understand, can you please ask again, I'll try to answer better this time 🙃 \n \n" \
    #

    return random_responses.random_string()
