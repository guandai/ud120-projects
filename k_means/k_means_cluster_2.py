# SQL
# /* select users.gender, orders.`cc_auth_amount_cents`, deal_crm_data.deal_crm_category_id from users   */
# select
# count(orders.`cc_auth_amount_cents`) as number  , sum(orders.`cc_auth_amount_cents`) as total,
# CASE users.gender
#     WHEN 'male' THEN 1
#     WHEN 'female' THEN 2
# END as gender

# /* count(CASE users.gender
#     WHEN 'male' THEN 1
#     WHEN 'female' THEN 2
# END ) as gender */


# from users  
# join orders on users.id = orders.user_id
# /* join order_lines on orders.id = order_lines.order_id
# join deals on deals.id = order_lines.deal_id
# join deal_crm_data on deals.id = deal_crm_data.deal_id
# where deal_crm_data.deal_crm_category_id is not null */
# /* and   orders.cc_auth_amount_cents is not null */
# where users.id < 10000
#   group by users.id
# /*    group by users.gender */




#!/usr/bin/python 

import pickle
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from mpl_toolkits.mplot3d import Axes3D


f = open('dt_data', 'r')
X = []
for line in f:
    arr = line[:-1].split('\t')
    arr = map(lambda x: int(x), arr)
    X.append(arr)

# X = [[1,2,3],[2,2,3],[1,2,4],[1,6,3],[3,2,3],[1,2,5],[1,4,3],[3,2,3]]

# fig = plt.figure()
# ax = fig.gca(projection='3d')
for val in X:
    # s = ax.scatter(val[0], val[1], val[2])
    plt.scatter(val[0], val[1])

plt.show()


from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
preds =  kmeans.labels_


def Draw(preds, features):
    colors = ["b", "c", "k", "m", "g"]
    # fig = plt.figure()
    # ax = fig.gca(projection='3d')

    for idx, pred in enumerate(preds):
        # ax.scatter(features[idx][0], features[idx][1], features[idx][2], c=colors[preds[idx]])
        plt.scatter(features[idx][0], features[idx][1],  c=colors[preds[idx]])


    plt.show()


try:
    Draw(preds, X)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
