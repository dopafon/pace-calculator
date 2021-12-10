from webapp import app
from flask import render_template, flash, redirect, request
from webapp.forms import SwimForm, BikeForm
from webapp.pacecalc import *

def validate_pace_or_time(mode):
    if mode == 'swim':
        form = SwimForm()
        form.validate()
        if not form.swim_pace_time.data and not form.swim_race_time.data:
            flash('At least one of race or pace time must be set', 'error')
        elif form.swim_pace_time.data and form.swim_race_time.data:
            flash('Please specify ONLY "pace" OR "time"', 'error')
    if mode == 'bike':
        form = BikeForm()
        form.validate()
        if not form.bike_pace_time.data and not form.bike_race_time.data:
            flash('At least one of race or pace time must be set', 'error')
        elif form.bike_pace_time.data and form.bike_race_time.data:
            flash('Please specify ONLY "pace" OR "time"', 'error')
    else:
        return True


        
@app.route('/', methods=['GET'])
def homepage():
    #return redirect('/swim')
    return render_template('home.html')

@app.route('/swim', methods=['GET', 'POST'])
def swim():
    form = SwimForm()
    if form.swim_pace_time.data is not None:
        validate_pace_or_time('swim')
        if form.swim_pace_time.data != '':
            # get seconds from timestring in form
            pace_time_str = form.swim_pace_time.data
            pace_secs = get_secs_from_time(pace_time_str)
            swimtime = get_time_by_pace(pace_secs, form.distance.data)
            if form.showsplits.data is True:
                swimsplits = create_swimsplits(get_secs_from_time(swimtime), form.distance.data)            
                showsplits = True
            else:
                swimsplits = ''
                showsplits = False
            return render_template('swim.html', title='Swim',
                form=form,
                swimtime=swimtime,
                swimpace=convert_secs_to_time(pace_secs),
                swimsplits=swimsplits,
                showsplits=showsplits)
        elif form.swim_race_time.data is not None:
            if form.swim_race_time.data != '':
                race_time_str = form.swim_race_time.data
                race_time_secs = get_secs_from_time(race_time_str)
                pacetime = get_swimpace_by_time(form.distance.data, race_time_secs)
                if form.showsplits.data is True:
                    swimsplits = swimsplits = create_swimsplits(race_time_secs, form.distance.data)
                    showsplits = True
                else:
                    swimsplits = ''
                    showsplits = False
                return render_template('swim.html', title='Swim', 
                    form=form,
                    swimtime=convert_secs_to_time(race_time_secs),
                    swimpace=pacetime,
                    swimsplits=swimsplits,
                    showsplits=showsplits)
            else:
                return render_template('swim.html', title='Swim', form=form)    
        else:
            return render_template('swim.html', title='Swim', form=form)
    else:
        return render_template('swim.html', title='Swim', form=form)

@app.route('/bike', methods=['GET', 'POST'])
def bike():
    form = BikeForm()
    if form.bike_pace_time.data is not None:
        validate_pace_or_time('bike')
        if form.bike_pace_time.data != '':
            # get seconds from timestring in form
            pace_time_str = form.bike_pace_time.data
            pace_kmh = float(pace_time_str.replace(',','.'))
            biketime = get_biketime_by_pace(pace_kmh, form.distance.data)
            
            if form.showsplits.data is True:
                bikesplits = create_bikesplits(get_secs_from_time(biketime), form.distance.data)            
                showsplits = True
            else:
                bikesplits = ''
                showsplits = False

            return render_template('bike.html', title='Swim',
                form=form,
                biketime=biketime,
                bikepace=pace_kmh,
                bikesplits=bikesplits,
                showsplits=showsplits)
        elif form.bike_race_time.data is not None:
            if form.bike_race_time.data != '':
                race_time_str = form.bike_race_time.data
                race_time_secs = get_secs_from_time(race_time_str)
                distance = form.distance.data * 1000
                pacetime = round(get_bikepace_by_time(distance, race_time_secs), 2)
                
                if form.showsplits.data is True:
                    bikesplits = bikesplits = create_bikesplits(race_time_secs, form.distance.data)
                    showsplits = True
                else:
                    bikesplits = ''
                    showsplits = False
                
                return render_template('bike.html', title='Bike', 
                    form=form,
                    biketime=convert_secs_to_time(race_time_secs),
                    bikepace=pacetime,
                    bikesplits=bikesplits,
                    showsplits=showsplits)
            else:
                return render_template('bike.html', title='Bike', form=form)    
        else:
            return render_template('bike.html', title='Bike', form=form)
    else:
        return render_template('bike.html', title='Bike', form=form)
