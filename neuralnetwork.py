import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from math import floor, cell
from pylab import rcParams
from subprocess import check_output

math_df = pd.read_csv("input/student-mat.csv", sep=";")
port_df = pd.read_csv("input/student-por.csv", sep=";")

math_df["course"] = "math"
port_df["course"] = "portuguese"

merged_df = math_df.append(port_df)
merged_df.shape

merge_vector = ["school","sex","age","address",
                "famsize","Pstatus","Medu","Fedu",
                "Mjob","Fjob","reason","nursery","internet"]


merged_df = merged_df.sample(frac=1)
merged_df['alcohol'] = (merged_df.Walc * 2 + merged_df.Dalc * 5) / 7
merged_df['alcohol'] = merged_df.alcohol.map(lambda x: ceil(x))
merged_df['drinker'] = merged_df.alcohol.map(lambda x: "yes" if x > 2 else "no")

def encode(series):
  return pd.get_dummies(series.astype(str))

train_x = pd.get_dummies(merged_df.school)
train_x['age'] = merged_df.age
train_x['absences'] = merged_df.absences
train_x['g1'] = merged_df.G1
train_x['g2'] = merged_df.G2
train_x['g3'] = merged_df.G3
train_x = pd.concat([train_x, encode(merged_df.sex), encode(merged_df.Pstatus),
                     encode(merged_df.Medu), encode(merged_df.Fedu),
                     encode(merged_df.guardian), encode(merged_df.studytime),
                     encode(merged_df.failures), encode(merged_df.activities),
                     encode(merged_df.higher), encode(merged_df.romantic),
                     encode(merged_df.reason), encode(merged_df.paid),
                     encode(merged_df.goout), encode(merged_df.health),
                     encode(merged_df.famsize), encode(merged_df.course)
                    ], axis=1)

train_y = encode(merged_df.drinker)

train_size = 0.9

train_cnt = floor(train_x.shape[0] * train_size)
x_train = train_x.iloc[0:train_cnt].values
y_train = train_y.iloc[0:train_cnt].values
x_test = train_x.iloc[train_cnt:].values
y_test = train_y.iloc[train_cnt:].values

def multilayer_perceptron(x, weights, biases, keep_prob):
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    layer_1 = tf.nn.dropout(layer_1, keep_prob)
    out_layer = tf.matmul(layer_1, weights['out']) + biases['out']
    return out_layer


n_hidden_1 = 38
n_input = train_x.shape[1]
n_classes = train_y.shape[1]

weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'out': tf.Variable(tf.random_normal([n_hidden_1, n_classes]))
}

biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

keep_prob = tf.placeholder("float")

training_epochs = 5000
display_step = 1000
batch_size = 32

x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_classes])

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predictions, labels=y))

optimizer = tf.train.AdamOptimizer(learning_rate=0.0001).minimize(cost)

predictions = multilayer_perceptron(x, weights, biases, keep_prob)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(training_epochs):
        avg_cost = 0.0
        total_batch = int(len(x_train) / batch_size)
        x_batches = np.array_split(x_train, total_batch)
        y_batches = np.array_split(y_train, total_batch)
        for i in range(total_batch):
            batch_x, batch_y = x_batches[i], y_batches[i]
            _, c = sess.run([optimizer, cost],
                            feed_dict={
                                x: batch_x,
                                y: batch_y,
                                keep_prob: 0.8
                            })
            avg_cost += c / total_batch
        if epoch % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost=", \
                "{:.9f}".format(avg_cost))
    print("Optimization Finished!")
    correct_prediction = tf.equal(tf.argmax(predictions, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print("Accuracy:", accuracy.eval({x: x_test, y: y_test, keep_prob: 1.0}))
