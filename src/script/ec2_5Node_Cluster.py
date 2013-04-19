from boto.ec2.connection import EC2Connection

import time

SERVER_TYPES = {
				'ec2' : {
						'placement' : 'us-east-1a',
						'image_id' : 'ami-3275ee5b',
						'instance_type' : 't1.micro',
						'security_groups' : ['quick-start-1'],
						'key_name' : 'ec2_anuvinda',
						'min_count' : 1,
						'max_count' : 5,
						},
}

class EC2Conn:

	def __init__(self):
		self.conn = None
		self.access_key = 'AKIAJE6VE6PP4G4PU4JQ'
		self.secret_key = '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'
		print 'Keys are provided'
		
	def connect(self):
		self.conn = EC2Connection(self.access_key, self.secret_key)
	
	def create_instance(self, instance_type='ec2'):
			reservation = self.conn.run_instances( **SERVER_TYPES [instance_type])
			print reservation
			for instance in reservation.instances:
				time.sleep(10)
				while instance.state != 'running':
					time.sleep(5)
					instance.update()
					print "Instance state: %s" % (instance.state)
				print "instance %s done!" % (instance.id)
		
def main():
	a = EC2Conn()
        a.connect()
        return a.create_instance()

if __name__ == '__main__':
    main()
	