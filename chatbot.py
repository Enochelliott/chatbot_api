from flask import Flask, request, jsonify

app = Flask(__name__)

def chatbot_response(user_input):
    input_lower = user_input.lower()
    
    keyword_responses = {
        'chart of accounts': {
            'keywords': ['chart of accounts', 'coa', 'help to find coa', 'help finding a chart of accounts', 
                         'need chart of accounts', 'need coa'],
            'response': "This information explains the Chart of Accounts.\nCOA/Chart of Accounts is simply a list of account names that a company uses in its general ledger for recording various business transactions"
        },
        'registry': {
            'keywords': ['registry', 'find registry', 'help with registry', 'need registry', 'what is registry'],
            'response': "This information explains the Registry.\nA recording of financial events that tracks (cash & checks) transactions for your business"
        },
        'transactions': {
            'keywords': ['transactions', 'find transactions', 'help to find transactions', 
                         'help with transactions', 'need transactions', 'what is transactions'],
            'response': "This information explains the Transactions.\nA transaction involves a monetary exchange for a good or service"
        },
        'customer': {
            'keywords': ['customer', 'find customer', 'help to find customer', 'help with customer', 
                         'need customer', 'what is customer'],
            'response': "This information explains what is a customer.\nA customer is an individual or business that purchases another company's goods or services"
        },
        'offerings': {
            'keywords': ['offerings', 'find offerings', 'help to find offerings', 'help with offerings', 
                         'need offerings', 'what is offerings'],
            'response': "This information explains what is a Offerings.\nOfferings are a category attached to the invoice for service or product"
        }
    }
    
    for category, data in keyword_responses.items():
        for keyword in data['keywords']:
            if keyword in input_lower:
                return data['response']
    
    return "I'm sorry, I didn't understand your request. Could you please try again with different wording?"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)
