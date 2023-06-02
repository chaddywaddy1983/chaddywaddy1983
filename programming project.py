class ticket:
    TicketList=[]
    def closedTicket(self):
        status=self.ticket_status
        
    def __init__(self,ticket_number,ticket_creator_name,staffID,contact_email,description,response,ticket_status):
        self.ticket_number = ticket_number
        self.ticket_creator_name = ticket_creator_name
        self.staffID = staffID
        self.contact_email = contact_email
        self.description = description
        self.response = response
        self.ticket_status = ticket_status

    def change_password (self):
        Des=self.description
        staff=self.staffID
        creatorN=self.ticket_creator_name
        if Des== "password Change":
            return staff[0]+staff[1]+creatorN[0]+creatorN[1]+creatorN[2]
        
    def response_ticket (self):
        TNo1 = int(input("Enter a ticket number:"))
        print("Enter a ticket number:", TNo1)

        ticket_creator_name1 = input("Enter the ticket creators name:")
        print("ticket creator name:", ticket_creator_name1)
        staffID1 = input("Enter staffID:")
        print("staffID:", staffID1)

        contact_email1 = input("Enter email address:")
        print("email address:", contact_email1)

        description1 = input("Enter decription of issue:")
        print("decription of issue:", description1)

        response1 = input("response:")
        print("response:", response1)

        ticket_status = input("ticket status:")
        print("ticket status", ticket_status)

        ticket1=ticket(TNo1,ticket_creator_name1,)
        TicketList.append(ticket1)










