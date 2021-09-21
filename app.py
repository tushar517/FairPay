from flask import Flask,request,render_template
from flask_cors import cross_origin
import sklearn
import pickle,jsonify
import pandas as pd
from flask_restful import Resource,Api,reqparse
app=Flask(__name__)
api=Api(app)
model=pickle.load(open("flight_rf.pkl","rb"))
class Predict(Resource):
    def post(self):
        #date_of_Journey
        data_dep=str(request.args["Dep_time"])
        Total_stops=int(request.args["stops"]) 
        airline=str(request.args['airline'])
        source=str(request.args["Source"])
        destination=str(request.args["Destination"])
        date_arr=str(request.args["Arrival_Time"])
        
        Journey_day=int(pd.to_datetime(data_dep,format="%Y-%m-%dT%H:%M").day)
        Journey_month=int(pd.to_datetime(data_dep,format="%Y-%m-%dT%H:%M").month)
            #print("Journey Date:",Journey_month)

            #departure
        Dep_hour=int(pd.to_datetime(data_dep,format="%Y-%m-%dT%H:%M").hour)
        Dep_min=int(pd.to_datetime(data_dep,format="%Y-%m-%dT%H:%M").minute)

            #Arrival
        
        Arrival_hour=int(pd.to_datetime(date_arr,format="%Y-%m-%dT%H:%M").hour)
        Arrival_min=int(pd.to_datetime(data_dep,format="%Y-%m-%dT%H:%M").minute)
            #print("Arrival: ",Arrival_hour,Arrival_min)
        print(Total_stops,airline,source,destination)
            #Duration
        dur_hour=abs(Arrival_hour-Dep_hour)
        dur_min=abs(Arrival_min- Dep_min)
            #print("Duration:",dur_hour,dur_min)

            #total stops
                                                    


            #Airline
            #AIR ASIA=0(not in the column)
            

        if(airline=='Jet Airways'):
            Jet_Airways=1
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(airline=='IndiGo'):
            Jet_Airways=0
            IndiGo=1
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0
            
        elif(airline=="Air India"):
            Jet_Airways=0
            IndiGo=0
            Air_India=1
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(airline=="Multiple carriers"):
            Jet_Airways=1
            IndiGo=0
            Air_India=0
            Multiple_carriers=1
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(airline=="SpiceJet"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=1
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(airline=="Vistara"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=1
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0
        
        elif(airline=="GoAir"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=1
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(airline=="Multiple_carriers_Premium_economy"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=1
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0
        
        elif(airline=="Jet Airways Business"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=1
            Vistara_Premium_economy=0
            Trujet=0

        elif(airline=="Vistara Premium economy"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=1
            Trujet=0
        
        elif(airline=='Trujet'):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=1

        else:
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        #Source
        #Banglore=0(not in column)

        

        if(source=="Delhi"):
            s_Delhi=1
            s_Kolkata=0
            s_Mumbai=0
            s_Chennai=0

        elif(source=="Kolkata"):
            s_Delhi=0
            s_Kolkata=1
            s_Mumbai=0
            s_Chennai=0

        elif(source=="Chennai"):
            s_Delhi=0
            s_Kolkata=0
            s_Mumbai=0
            s_Chennai=1

        elif(source=="Mumbai"):
            s_Delhi=0
            s_Kolkata=0
            s_Mumbai=1
            s_Chennai=0

        else:
            s_Delhi=0
            s_Kolkata=0
            s_Mumbai=0
            s_Chennai=0

        #Destination
        #Banglore=0(not in the column)

        
        if(destination=="Cochin"):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif(destination=="Delhi"):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
        elif(destination=="New delhi"):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif(destination=="Hyderabad"):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0 

        elif(destination=="Kolkata"):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']

        prediction=model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]])
        output=prediction[0]
        response={
            'response':str(output)
        }
        return response
api.add_resource(Predict,'/predict')
if __name__=="__main__": 
    app.run(debug=True)
    


        