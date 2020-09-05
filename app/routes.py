from app import app
from flask import render_template, flash, redirect, request
from app.forms import CalcForm
from app.pacecalc import get_swimpace_by_time, get_time_by_pace, get_secs_from_time, convert_secs_to_time, create_swimsplits

@app.route('/', methods=['GET'])
def homepage():
    return redirect('/swim')

@app.route('/swim', methods=['GET', 'POST'])
def swim():
    form = CalcForm()
    #if form.validate_on_submit():
    #    flash('Distance {}, pace {}'.format(
    #        form.distance.data, form.pace_time.data))
    #    return redirect('/')
    if form.swim_pace_time.data is not None:
        if form.swim_pace_time.data != '':
            # get seconds from timestring in form
            pace_time_str = form.swim_pace_time.data
            pace_secs = get_secs_from_time(pace_time_str)
            swimtime = get_time_by_pace(pace_secs, form.distance.data)
            swimsplits = create_swimsplits(get_secs_from_time(swimtime), form.distance.data)
            return render_template('swim.html', title='Swim',
                form=form,
                swimtime=swimtime,
                swimpace=convert_secs_to_time(pace_secs),
                swimsplits=swimsplits)
        elif form.swim_race_time.data is not None:
            if form.swim_race_time.data != '':
                race_time_str = form.swim_race_time.data
                race_time_secs = get_secs_from_time(race_time_str)
                pacetime = get_swimpace_by_time(form.distance.data, race_time_secs)
                swimsplits = create_swimsplits(race_time_secs, form.distance.data)
                return render_template('swim.html', title='Swim', 
                    form=form,
                    swimtime=convert_secs_to_time(race_time_secs),
                    swimpace=pacetime, swimsplits=swimsplits)
            else:
                return render_template('swim.html', title='Swim', form=form)    
        else:
            return render_template('swim.html', title='Swim', form=form)
    else:
        return render_template('swim.html', title='Swim', form=form)