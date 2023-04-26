package airpollutionseoul_q2;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class AirPollutionSeoul_q2_Mapper extends Mapper<Object, Text, Text, IntWritable>{

	Text station_code = new Text();
	IntWritable output_value = new IntWritable(1);
	boolean is_head = true;

	protected void map(Object key, Text value, Mapper<Object, Text, Text, IntWritable>.Context context)
			throws IOException, InterruptedException {
		// first line is head
		if(is_head)	{
			is_head = false;
			return;
		}

		// read line
		// colums = [time, station_code, item code, value, instrument status]
		String[] colums = value.toString().split(",");

		// Instrument status 0: Normal
		if(Integer.parseInt(colums[4]) == 0){
			// Item code 8: PM10
			if(Integer.parseInt(colums[2]) == 8){
				// if PM10 value <= 30, air condition is good
				if(Float.parseFloat(colums[3]) <= 30) {
					// set @station_code
					station_code.set(colums[1]);
					// write context
					context.write(station_code, output_value);
				}
			}
			// Item code 9: PM2.5
			else if(Integer.parseInt(colums[2]) == 9) {
				// if PM2.5 value <= 15, air condition is good
				if(Float.parseFloat(colums[3]) <= 15){
					station_code.set(colums[1]);
					// write context
					context.write(station_code, output_value);
				}
			}
		}
	}
}
