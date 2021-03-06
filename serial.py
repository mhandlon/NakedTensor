#  Fit a straight line, of the form y=m*x+b

import tensorflow as tf

xs = [ 0.00,  1.00,  2.00, 3.00, 4.00, 5.00, 6.00, 7.00] # Features
ys = [-0.82, -0.94, -0.12, 0.26, 0.39, 0.64, 1.02, 1.00] # Labels

m_initial = -0.5 # Initial guesses
b_initial =  1.0

m = tf.Variable(m_initial) # Parameters
b = tf.Variable(b_initial)

error = 0.0
for i in range(len(xs)):
	y_model = m*xs[i]+b # Output of the model
	error += (ys[i]-y_model)**2 # Difference squared

operation = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(error) # Does one step

with tf.Session() as session:
	session.run(tf.initialize_all_variables()) # Initialize session

	for iteration in range(10000):
		session.run(operation)

	print('Slope:', m.eval(), 'Intercept:', b.eval())

