NYC-Bridges-and-Tunnels-Traffic-Data
====================================

Visualization of NYC MTA's open data set of daily traffic on MTA bridges and tunnel

Motivation: To find trends in the number of vehicles that pass through toll bridges and tunnels in NYC.


  A couple of interesting trends were found simply through inspection. Figure 1 is the plot for total cash count of everyday through the 10 toll locations for a the weeks between 5/5/14 to 6/9/14, similary figure 2 is the total electronic count. It seems that each week the number of vehicles decreases from the beginning of the week (sunday) reaching the minimum value on wednesday and rises again reaching the maximum value on saturday. Comparatively electronic count of vehicles is more constant throughout the week. A possible explanation could be regular commuters of NYC use electronic payment methods such as ez-pass and tourists visting NYC use cash so there is an increase of vehicles through cash toll booths during the weekend. 

Figure 1:
![Alt text](/Plots/Cash Count for Weeks 5-5-14 to 6-9-14.png "Cash Count for Weeks 5-5-14 to 6-9-14")

Figure 2:
![Alt text](/Plots/Electronic Count for Weeks 5-5-14 to 6-9-14.png "Electronic Count for Weeks 5-5-14 to 6-9-14")  
  
  Another interesting note is seen in the huge difference between the y-axis scale for the time period studied. Electronic payments are nearly 10 times those of cash payments. This observation is consistent with the trend of declining usage of cash in the American society. 
   
  The last trend that is immediately obvious is seen using the data set year. It holds data points for the same week for the past three years. (The plots can be generated by changing the datafile variable in the python script.) By studying the electronic payments graph, it seems that the over the years the number of vehicles going through he toll booths are decreasing. 

