import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key = "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"

# GRAB DATE-----------------------------------------
def gen_prompt_date(textdata):
    return """Return the due date from the text provided.

    Text: STATE OF NEW YORKBID NUMBER92046-06083-108COUNTY OF NASSAU     Ad Date:05/25/2023BIDSWILL BE RECEIVED AND OPENED AT         BID OPENING DATEOFFICE OF PURCHASING, 1 WEST STREET,06/08/2023NORTH ENTRANCE, MINEOLA, NEW YORK  1150111:00 A.M. E.S.T.OFFICE HOURS 9 AM –NOON & 1 PM –4:45 PMBUYER:TELEPHONE:REQUISITION NUMBERKimberly Stanton(516) 571-6679RQIT23000136
    Due Date: June 08 2023
    Text: {}
    Due Date:""".format(textdata.capitalize())

# GRAB CONTACT INFO-----------------------------------------
def gen_prompt_contact(textdata):
    return """Return the person to contact from the text provided. Contact information may be an email address and/or a telephone number.

    Text: STATE OF NEW YORKBID NUMBER92046-06083-108COUNTY OF NASSAU     Ad Date:05/25/2023BIDSWILL BE RECEIVED AND OPENED AT         BID OPENING DATEOFFICE OF PURCHASING, 1 WEST STREET,06/08/2023NORTH ENTRANCE, MINEOLA, NEW YORK  1150111:00 A.M. E.S.T.OFFICE HOURS 9 AM –NOON & 1 PM –4:45 PMBUYER:TELEPHONE:REQUISITION NUMBERKimberly Stanton(516) 571-6679RQIT23000136
    Name and Contact Info: Kimberly Stanton, (516) 571-6679
    Text: {}
    Name and Contact Info:""".format(textdata.capitalize())

# GRAB MODE OF DELIVERY + WHERE-----------------------------------------
def gen_prompt_delivery(textdata):
    return """Return the method of delivery for the bid, and where to deliver it. Something along the lines of "bids will be received and opened at" and/or an address provided
                means the method is mail. Then say mail and list the address.
                If a website URL is provided, the method is online. Say online and list the URL.
                If only email addresses are provided, the method is email. Say email and list the email address.

    Text: STATE OF NEW YORKBID NUMBER92046-06083-108COUNTY OF NASSAU     Ad Date:05/25/2023BIDSWILL BE RECEIVED AND OPENED AT         BID OPENING DATEOFFICE OF PURCHASING, 1 WEST STREET,06/08/2023NORTH ENTRANCE, MINEOLA, NEW YORK  1150111:00 A.M. E.S.T.OFFICE HOURS 9 AM –NOON & 1 PM –4:45 PMBUYER:TELEPHONE:REQUISITION NUMBERKimberly Stanton(516) 571-6679RQIT23000136PREPARE YOUR BID ON THIS FORM USING BLACK INK OR TYPEWRITERBIDTITLE:   AUTOCAD SUBSCRIPTION LICENSE & SUPPORT● ALL BIDS MUST BE F.O.B. DESTINATION ANDINCLUDE DELIVERY WITHIN DOORS UNLESS OTHERWISE SPECIFIEDTHE UNDERSIGNED BIDDER AFFIRMS AND DECLARES THAT HE/SHE HAS CAREFULLY EXAMINED THE ADVERTISED INVITATION FOR BIDS, THE BID TERMS AND CONDITIONS, AND DETAILED SPECIFICATIONS, AND CERTIFIES THAT THIS BID IS SIGNED WITH FULL KNOWLEDGE AND ACCEPTANCE OF ALL THE PROVISIONS THEREOF AND OFFERS AND AGREES, IF THIS BID IS ACCEPTED WITHIN NINETY (90) DAYS FROM THE BID OPENING DATE TO FURNISH ANY OR ALL THE ITEMS UPON WHICH PRICES ARE HEREINAFTER QUOTEDIN THE QUANTITY AND AT THE PRICES BID.CASH DISCOUNT OF ________ PERCENT WILL BE ALLOWED FOR PROMPT PAYMENT WITHIN 20 BUSINESS DAYS.THE BIDDER CERTIFIES THAT: (A) THE BID HAS BEEN ARRIVED AT BY THE BIDDER INDEPENDENTLY AND HAS BEEN SUBMITTEDWITHOUTCOLLUSION WITH ANY OTHER VENDOR OF MATERIALS, SUPPLIES OR EQUIPMENT OF THE TYPE DESCRIBED IN INVITA-TION FOR BIDS, AND (B) THE CONTENTS OF THE BID HAVE NOT BEEN COMMUNICATED BY THE BIDDER, NOR, TO ITS BESTKNOWLEDGE AND BELIEF, BY ANY OF ITS EMPLOYEES OR AGENTS, TO ANY PERSON NOT AN EMPLOYEE OR AGENT OF BIDDER OR ITS SURETY ON ANY BOND FURNISHED HEREWITH PRIOR TO OFFICIAL OPENING OF THE BID.DELIVERY MADE TO:DEPARTMENT OF INFORMATION TECHNOLOGY240 OLD COUNTRY ROADMINEOLS, NY 11501GUARANTEED DELIVERY DATE__________________DAYS AFTER RECEIPT OF ORDEREMPLOYERS FEDERAL TAX ID NUMBER
    Deliver By: Mail, 240 OLD COUNTRY ROADMINEOLS, NY 11501
    Text: {}
    Deliver By:""".format(textdata.capitalize())

# GRAB COMMODITIES-----------------------------------------
def gen_prompt_commodities(textdata):
    return """Return what product(s) the company is asking for.

    Text: STATE OF NEW YORKBID NUMBER92046-06083-108COUNTY OF NASSAU     Ad Date:05/25/2023BIDSWILL BE RECEIVED AND OPENED AT         BID OPENING DATEOFFICE OF PURCHASING, 1 WEST STREET,06/08/2023NORTH ENTRANCE, MINEOLA, NEW YORK  1150111:00 A.M. E.S.T.OFFICE HOURS 9 AM –NOON & 1 PM –4:45 PMBUYER:TELEPHONE:REQUISITION NUMBERKimberly Stanton(516) 571-6679RQIT23000136PREPARE YOUR BID ON THIS FORM USING BLACK INK OR TYPEWRITERBIDTITLE:   AUTOCAD SUBSCRIPTION LICENSE & SUPPORT● ALL BIDS MUST BE F.O.B. DESTINATION ANDINCLUDE DELIVERY WITHIN DOORS UNLESS OTHERWISE SPECIFIEDTHE UNDERSIGNED BIDDER AFFIRMS AND DECLARES THAT HE/SHE HAS CAREFULLY EXAMINED THE ADVERTISED INVITATION FOR BIDS, THE BID TERMS AND CONDITIONS, AND DETAILED SPECIFICATIONS, AND CERTIFIES THAT THIS BID IS SIGNED WITH FULL KNOWLEDGE AND ACCEPTANCE OF ALL THE PROVISIONS THEREOF AND OFFERS AND AGREES, IF THIS BID IS ACCEPTED WITHIN NINETY (90) DAYS FROM THE BID OPENING DATE TO FURNISH ANY OR ALL THE ITEMS UPON WHICH PRICES ARE HEREINAFTER QUOTEDIN THE QUANTITY AND AT THE PRICES BID.CASH DISCOUNT OF ________ PERCENT WILL BE ALLOWED FOR PROMPT PAYMENT WITHIN 20 BUSINESS DAYS.THE BIDDER CERTIFIES THAT: (A) THE BID HAS BEEN ARRIVED AT BY THE BIDDER INDEPENDENTLY AND HAS BEEN SUBMITTEDWITHOUTCOLLUSION WITH ANY OTHER VENDOR OF MATERIALS, SUPPLIES OR EQUIPMENT OF THE TYPE DESCRIBED IN INVITA-TION FOR BIDS, AND (B) THE CONTENTS OF THE BID HAVE NOT BEEN COMMUNICATED BY THE BIDDER, NOR, TO ITS BESTKNOWLEDGE AND BELIEF, BY ANY OF ITS EMPLOYEES OR AGENTS, TO ANY PERSON NOT AN EMPLOYEE OR AGENT OF BIDDER OR ITS SURETY ON ANY BOND FURNISHED HEREWITH PRIOR TO OFFICIAL OPENING OF THE BID.DELIVERY MADE TO:DEPARTMENT OF INFORMATION TECHNOLOGY240 OLD COUNTRY ROADMINEOLS, NY 11501GUARANTEED DELIVERY DATE__________________DAYS AFTER RECEIPT OF ORDEREMPLOYERS FEDERAL TAX ID NUMBER
    Commodity: AUTOCAD SUBSCRIPTION LICENSE & SUPPORT
    Text: {}
    Commodity:""".format(textdata.capitalize())

lines_printed = 0

folder_path = "./textfiles"
os.makedirs(folder_path, exist_ok=True)

# Iterate through files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if os.path.isfile(file_path):

        with open(file_path, "r") as file:
            file_data = file.read()

        date_response = openai.Completion.create(
            model="text-davinci-003",
            prompt= gen_prompt_date(file_data),
            temperature=0,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        contact_response = openai.Completion.create(
            model="text-davinci-003",
            prompt= gen_prompt_contact(file_data),
            temperature=0,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )


        delivery_response = openai.Completion.create(
            model="text-davinci-003",
            prompt= gen_prompt_delivery(file_data),
            temperature=0,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        commodity_response = openai.Completion.create(
            model="text-davinci-003",
            prompt= gen_prompt_commodities(file_data),
            temperature=0,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )


print(date_response.choices[0].text)
print(contact_response.choices[0].text)
print(delivery_response.choices[0].text)
print(commodity_response.choices[0].text)


        

