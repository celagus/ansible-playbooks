# *** IMPORTANT DISCLAIMER ***
# This API is for Lab purposes, DON'T USE IT FOR PRODUCTION, UNLESS IT WERE HARDENED!!!!
#

from flask import Flask, request
from flask_restful import Resource, Api

import subprocess

app = Flask(__name__)
api = Api(app)

actions = ['baja']

def query():
        user = request.args.get('user')
        action = request.args.get('action')
        if (action in actions):
                return user
        else:
                raise ValueError

@app.route('/ansible/', methods=['POST','GET'])

def get_status():
        user = query()
        try:
            result_success = subprocess.Popen("ansible-playbook /etc/ansible/playbooks/del_user.yml --extra-vars apiUser="+user, shell=True, stdout=subprocess.PIPE).stdout.read()
            return result_success
        except subprocess.CalledProcessError as e:
            return "An error occurred while trying to fetch task status updates."

        return 'Success %s' % (result_success)

if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0')