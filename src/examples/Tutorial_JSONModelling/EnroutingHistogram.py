#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:16:56 2018

@author: isaaclera
"""

routes =[([13], 206), ([100], 443), ([67, 19, 2, 100], 235), ([100], 338), ([100], 599), ([100], 439), ([34, 93, 40], 283), ([62, 6], 484), ([100], 236), ([100], 384), ([72, 20, 0, 3, 30], 457), ([24, 5, 6, 60], 340), ([87, 1, 50], 409), ([100], 432), ([62, 5, 2, 100], 460), ([79], 580), ([87, 1, 2, 19], 427), ([62, 5, 2, 100], 537), ([33, 1, 4], 175), ([24, 5, 17], 568), ([100], 238), ([46], 392), ([100], 329), ([62, 6], 494), ([13, 35], 225), ([100], 142), ([87], 417), ([100], 311), ([100], 245), ([100], 444), ([100], 144), ([81, 2, 100], 601), ([31, 41, 97], 191), ([100], 247), ([99, 6, 47, 66], 470), ([100], 524), ([100], 146), ([100], 591), ([38, 7, 2, 100], 592), ([83, 70, 2, 79], 572), ([81, 2, 100], 440), ([44], 231), ([46], 424), ([87, 1, 4, 8], 476), ([40, 76], 287), ([100], 306), ([100], 448), ([24, 5, 2, 100], 304), ([0, 2, 19], 421), ([77, 50, 1, 5, 90], 278), ([93, 40, 0, 8], 476), ([100], 589), ([100], 594), ([100], 250), ([100], 321), ([46, 2, 57], 401), ([46, 2, 100], 601), ([100], 137), ([100], 158), ([36, 20, 0, 8, 73], 464), ([33, 1, 2, 100], 523), ([58, 12, 2, 20, 32], 449), ([23, 28, 0, 68, 16], 263), ([50, 25, 70, 73], 464), ([97, 41], 226), ([65, 29], 507), ([100], 442), ([100], 585), ([46, 2, 19], 427), ([26, 2, 3], 370), ([96, 4, 2, 100], 314), ([100], 540), ([99, 28], 257), ([100], 522), ([33, 1, 2, 100], 528), ([96, 4, 2, 79], 572), ([100], 317), ([61, 16, 6, 99], 255), ([100], 307), ([46, 2, 12], 416), ([87, 1, 2, 6, 99], 255), ([52, 5, 2, 100], 275), ([12, 2, 100], 322), ([100], 441), ([100], 605), ([40, 93], 296), ([7, 17], 560), ([52, 5, 2, 100], 528), ([100], 243), ([13, 2, 20, 36], 211), ([100], 336), ([67, 19, 72], 455), ([4, 8, 51], 348), ([21, 5, 2, 100], 252), ([100], 145), ([0, 2], 395), ([44, 2, 100], 440), ([79, 71], 554), ([46, 2], 411), ([100], 148), ([93, 40, 0, 2, 100], 139), ([17, 5, 2, 100], 153), ([100], 600), ([87, 1, 2], 403), ([46, 2], 395), ([100], 390), ([100], 308), ([100], 538), ([32], 452), ([100], 586), ([100], 607), ([44, 2, 100], 543), ([100], 309), ([14, 2, 100], 275), ([67, 19, 2, 100], 314), ([33, 1, 87], 393), ([100], 157), ([73, 8, 0, 28, 99], 468), ([100], 312), ([100], 254), ([100], 337), ([100], 598), ([61, 16, 6, 60], 340), ([0, 2, 46], 408), ([100], 527), ([0, 2, 19], 427), ([100], 248), ([99, 6, 2, 69], 261), ([100], 160), ([96, 4, 2, 100], 379), ([100], 324), ([0, 2, 12], 416), ([32, 20, 2, 100], 601), ([100], 138), ([100], 159), ([100], 445), ([71, 2, 100], 601), ([100], 315), ([100], 246), ([52, 5, 2, 100], 235), ([100], 525), ([100], 544), ([100], 381), ([100], 150), ([51], 360), ([13], 218), ([100], 305), ([100], 249), ([98, 2, 6, 60], 340), ([100], 588), ([100], 593), ([4, 8, 51], 364), ([98, 2, 100], 583), ([40], 301), ([100], 383), ([98, 2, 12], 495), ([100], 154), ([100], 595), ([61, 16, 5, 2, 100], 528), ([20], 561), ([98, 2, 100], 242), ([4, 2, 29, 65], 356), ([100], 437), ([34, 93, 40, 90], 293), ([46, 2, 100], 537), ([50], 425), ([55, 2, 100], 139), ([71, 3], 376), ([8, 0], 482), ([100], 597), ([13, 22], 201), ([14, 2, 0], 391), ([14, 2, 100], 601), ([6, 29, 65], 502), ([100], 382), ([100], 333), ([65, 29, 2, 100], 583), ([83, 70, 2, 100], 162), ([100], 240), ([58, 12, 2, 6, 99], 255), ([100], 319), ([88, 28, 0, 2, 100], 242), ([100], 519), ([83, 70, 73, 8, 32], 273), ([36, 20, 44], 577), ([100], 164), ([83, 70, 87], 393), ([100], 140), ([71, 79], 572), ([90, 40, 93, 34], 280), ([100], 596), ([100], 386), ([77, 57, 2, 100], 242), ([44, 20], 552), ([87, 1, 2], 411), ([71, 2, 100], 543), ([100], 147), ([16, 5, 2, 70, 83], 269), ([14, 2, 6, 36], 461), ([87, 1], 419), ([31, 41], 195), ([61, 16, 5, 2, 100], 537), ([40, 0, 15], 298), ([100], 328), ([100], 325), ([31, 41, 97], 185), ([100], 251), ([100], 141), ([100], 529), ([100], 327), ([34, 93, 40], 289), ([96, 70, 87], 393), ([52, 5, 17], 568), ([62, 5, 2, 3], 376), ([100], 156), ([87, 1, 50], 400), ([4, 2, 100], 388), ([100], 387), ([64, 3, 2, 100], 601), ([100], 435), ([98, 2, 0], 482), ([81, 98], 480), ([52, 5, 2, 19, 72], 455), ([52, 5, 90], 278), ([46, 2, 100], 433), ([24, 5, 2, 100], 537), ([16, 6, 60, 27], 265), ([58, 12, 2, 100], 314), ([100], 330), ([100], 318), ([100], 323), ([81, 2, 100], 242), ([77, 57, 2, 100], 304), ([87, 1, 2, 100], 601), ([100], 606), ([44, 20, 36], 569), ([100], 320), ([100], 431), ([27], 267), ([0, 2, 6], 488), ([97, 41, 31], 177), ([100], 276), ([7, 2, 100], 149), ([97, 27, 19, 53], 212), ([46, 2, 98], 480), ([4, 2, 44], 189), ([100], 237), ([33, 1, 5, 90], 278), ([100], 241), ([100], 436), ([100], 584), ([52, 5, 2, 100], 601), ([77, 57, 2, 100], 543), ([100], 380), ([0, 2], 403), ([46], 408), ([100], 151), ([100], 539), ([44, 2, 100], 583), ([100], 587), ([87, 1, 2, 100], 592), ([100], 310), ([24, 5, 46], 392), ([71], 562), ([6], 488), ([0, 2], 411), ([33, 1, 50], 462), ([3, 0, 40, 93], 374), ([100], 313), ([8, 86, 6], 494), ([46, 2, 100], 316), ([100], 518), ([46, 2], 403), ([31], 219), ([4, 1], 351), ([100], 434), ([100], 459), ([87, 1, 5, 17], 568), ([100], 389), ([100], 332), ([97, 41, 2, 6, 99], 255), ([100], 143), ([98, 2, 100], 275), ([29], 513), ([100], 603), ([4, 13], 181), ([100], 163), ([100], 334), ([100], 446), ([3, 2, 26], 367), ([60, 6, 2, 4], 343), ([100], 385), ([87, 1, 2, 100], 235), ([83, 70, 2, 100], 242), ([4, 13], 194), ([100], 520), ([100], 526), ([100], 541), ([97, 41, 2, 100], 583), ([98], 480), ([62], 479), ([100], 161), ([55, 2, 19, 72], 455), ([46, 2, 19], 421), ([93, 40, 0, 2, 100], 543), ([100], 604), ([41, 31], 207), ([23, 20, 2, 19, 89], 271), ([100], 530), ([97, 41, 2, 98], 480), ([71, 2, 20, 32], 449), ([100], 155), ([66], 473), ([0, 2, 57], 401), ([100], 326), ([100], 244), ([55, 2, 3], 376), ([97, 41, 2, 100], 242), ([100], 438), ([64, 3, 2, 100], 583), ([67, 19, 2, 100], 601), ([17, 7], 551), ([87, 1, 2], 395), ([83, 70, 2, 100], 136), ([32, 20, 2, 100], 583), ([100], 521), ([100], 447), ([100], 542), ([58, 12, 2, 100], 379), ([52, 5, 2, 100], 304), ([97, 41, 2, 0, 8], 199), ([100], 590), ([38, 7, 17], 568), ([61, 16, 5, 2, 100], 331), ([97], 233), ([17], 576), ([99, 28, 23], 259), ([100], 335), ([100], 253), ([100], 602), ([100], 152), ([46, 2, 100], 304), ([100], 239)]

routes = [([28, 99], 552), ([32, 20, 2, 13, 22], 294), ([47, 6], 418), ([35], 215), ([35], 223), ([53], 401), ([14, 2, 7], 519), ([70], 370), ([43], 178), ([15], 543), ([40], 177), ([5, 6, 36], 495), ([83, 70, 2, 7], 519), ([13], 264), ([44, 20, 36], 267), ([83, 70, 2, 9, 64], 79), ([29, 2], 201), ([19], 144), ([61], 308), ([87], 311), ([64, 9, 7], 519), ([57, 2, 9], 345), ([8, 66], 512), ([44], 277), ([43, 57], 329), ([44, 20, 36], 284), ([84], 480), ([76], 371), ([2], 213), ([87, 70, 73], 350), ([19], 141), ([15, 0, 8], 384), ([93], 220), ([87, 1], 166), ([14], 167), ([29], 210), ([7, 17], 420), ([93, 40], 182), ([46], 206), ([44], 291), ([56, 15, 37, 61], 207), ([6], 448), ([78], 124), ([83], 331), ([98], 428), ([99], 554), ([81, 98], 410), ([60], 503), ([7, 2, 13, 35], 525), ([9], 396), ([38], 301), ([0], 429), ([2], 229), ([12, 2, 0], 411), ([43], 188), ([5], 364), ([73, 70, 83], 381), ([98], 452), ([24], 246), ([46], 198), ([0, 2, 12], 419), ([38], 295), ([93, 40, 76], 361), ([35], 231), ([17], 455), ([18], 158), ([58, 12], 408), ([18, 26, 85], 151), ([71], 175), ([99], 557), ([22], 300), ([97], 127), ([62], 184), ([18], 162), ([17], 450), ([38], 298), ([73, 70], 360), ([14, 13], 244), ([44], 272), ([52, 5, 90], 312), ([18, 5, 2, 98], 157), ([93], 228), ([37, 61, 16, 22], 479), ([23, 28], 551), ([84], 481), ([81, 2, 0], 453), ([24, 9, 2, 44], 261), ([32, 20, 2, 9, 64], 79), ([35, 15, 56], 549), ([40, 76, 18], 152), ([83, 70, 73], 350), ([79, 2, 78], 119), ([9, 33], 385), ([81, 2, 9, 64], 79), ([67], 309), ([49, 25, 95, 79], 466), ([65, 47, 66, 8], 484), ([44, 20, 36], 280), ([99], 556), ([90, 5, 6], 395), ([88], 176), ([65, 47, 6], 407), ([44], 261), ([8, 73], 489), ([93], 212), ([32, 20, 2, 79], 88), ([2], 221), ([35, 13, 2, 7], 531), ([12], 444), ([23, 20, 2, 41], 237), ([67, 19, 94], 296), ([67, 27], 520), ([13, 45], 285), ([71, 3, 10], 304), ([93, 34], 202), ([99], 553), ([32], 137), ([93, 40, 90], 382), ([56, 3, 2], 209), ([67, 19, 2, 0, 8], 484), ([16], 80), ([31, 41, 97], 122), ([6], 424), ([58, 43, 19], 133), ([18], 152), ([43], 315), ([88], 186), ([34], 233), ([24], 250), ([27, 25, 74, 15, 35], 525), ([17], 426), ([64, 9, 2, 13, 22], 294), ([8], 313), ([58, 43], 306), ([97], 117), ([61, 37, 0, 8], 333), ([49], 474), ([40, 0, 2, 98], 157), ([40], 172), ([47], 432), ([61, 37, 15], 325), ([87], 332), ([67], 318), ([8], 333), ([8, 73], 350), ([42], 465), ([60], 499), ([40, 93], 351), ([15, 6, 5], 344), ([49], 468), ([14, 13, 22], 294), ([87, 1, 2, 44], 247), ([14], 169), ([46, 2], 201), ([34], 214), ([67], 339), ([61, 37, 15, 56], 199), ([67, 19, 53], 349), ([62], 174), ([30], 560), ([43], 336), ([88], 196), ([33, 1, 2, 13, 35], 459), ([58, 12, 2, 0, 8], 484), ([52, 5, 18], 148), ([37, 15, 84], 478), ([43], 173), ([90], 322), ([87, 1, 25, 49], 471), ([8, 66], 493), ([29], 226), ([44], 251), ([13], 249), ([2], 225), ([33], 335), ([53], 359), ([58, 43], 183), ([66], 516), ([16], 82), ([6], 442), ([42], 467), ([19], 136), ([94], 299), ([44], 256), ([14], 171), ([60], 508), ([24], 276), ([40], 192), ([18, 26], 154), ([33], 305), ([34], 230), ([40, 0, 2, 26], 154), ([13], 254), ([24, 9], 269), ([79], 93), ([46], 234), ([35, 15, 49], 460), ([52, 5, 16], 78), ([41, 2, 69], 242), ([22], 297), ([36], 515), ([2], 217), ([32, 8, 0, 15, 49], 471), ([41, 2, 5, 62], 238), ([24], 290), ([96, 4, 2, 3, 30], 561), ([1], 168), ([61], 235), ([79, 2, 78], 101), ([49, 15, 42], 461), ([71], 185), ([87], 321), ([17], 445), ([85], 165), ([33], 314), ([42], 463), ([9], 365), ([5, 2, 70, 73], 489), ([31], 91), ([88], 191), ([41], 243), ([38, 7], 519), ([6, 47], 413), ([46, 2], 209), ([66], 509), ([99], 555), ([71], 190), ([17, 7], 412), ([49, 15], 464), ([9], 355), ([1], 170), ([88], 181), ([65], 236), ([83], 320), ([81, 98], 422), ([31, 41, 97], 103), ([19], 128), ([71], 195), ([26, 2, 3, 30], 559), ([98], 446), ([24, 5, 6, 36], 284), ([83], 340), ([7, 17], 431), ([84], 482), ([57], 389), ([40], 187), ([83, 70], 391), ([46, 2, 55], 403), ([67, 19, 2, 79], 88), ([5, 6, 36], 511), ([87, 1, 5, 16], 78), ([24, 5], 483), ([0, 2, 6], 435), ([90], 342), ([71], 180), ([31], 104), ([24, 5, 6, 36], 280), ([47], 456), ([8, 66], 496), ([0], 453), ([46, 2, 79], 88), ([40, 76], 392), ([62], 189), ([41], 240), ([40, 0, 2, 26, 85], 151), ([13, 45], 281), ([19, 43], 271), ([47, 6], 435), ([29], 218), ([32], 129), ([46, 2, 13, 22], 294), ([65, 29], 197), ([53], 380), ([13, 14], 259), ([87, 70], 391), ([81, 98], 440), ([8], 323), ([81], 434), ([52, 5, 12], 408), ([64], 81), ([98, 2, 19], 133), ([4, 2, 0], 411), ([41, 2, 69], 241), ([33, 1, 7], 519), ([79, 2, 78], 111), ([58, 12, 5, 16], 78), ([53], 369), ([13], 274), ([40, 93, 34], 160), ([12], 449), ([79, 2, 3, 56], 106), ([29, 65], 208), ([58, 43, 19], 245), ([43], 193), ([90, 40], 326), ([66], 504), ([9], 376), ([78], 115), ([32], 134), ([40, 76, 18], 158), ([18, 5, 2, 98], 161), ([19, 2, 44], 251), ([62], 179), ([33, 9], 324), ([31], 95), ([30, 3, 2, 26], 558), ([5, 90], 382), ([8], 384), ([5, 6, 60], 492), ([87, 1, 2, 79], 88), ([55], 404), ([98, 81], 415), ([96, 4], 406), ([55, 5, 90], 312), ([87], 341), ([65, 47, 66, 8], 303), ([32], 145), ([42], 462), ([35, 15, 56], 536), ([31, 41], 108), ([67], 390), ([10, 0, 8], 313), ([35, 15], 527), ([32], 142), ([64], 83), ([94], 302), ([61, 37, 0, 8], 313), ([71, 2, 19], 133), ([83, 70, 2, 3, 30], 561), ([67], 330), ([14, 2, 0, 40], 149), ([67, 19], 245), ([38, 25, 49], 471), ([83], 402), ([56, 15, 35], 203), ([5], 354), ([10], 334), ([13], 289), ([7, 17], 436), ([97, 41, 31], 85), ([10, 0, 8], 323), ([34], 222), ([93], 200), ([13], 270), ([12], 425), ([98, 2, 13, 22], 294), ([79], 97), ([62], 194), ([58, 12, 2, 7], 519), ([41], 239), ([24], 266), ([9], 345), ([24, 5, 21], 255), ([98, 2, 0, 37], 477), ([38, 7, 17], 409), ([83], 310), ([66], 500), ([15], 539), ([93, 34], 205), ([83, 70, 2, 79], 88)]
lastDevices=[]
for item in routes:
    lastDevices.append(item[0][-1])

import matplotlib.pyplot as plt
import numpy as np
print np.histogram(lastDevices,bins=range(101))
plt.hist(lastDevices, bins=100)  # arguments are passed to np.histogram
plt.title("Selection Histogram")
plt.show()
    