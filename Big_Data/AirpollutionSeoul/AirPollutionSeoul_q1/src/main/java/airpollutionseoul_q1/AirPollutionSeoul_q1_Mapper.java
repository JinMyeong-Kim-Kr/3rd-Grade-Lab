package airpollutionseoul_q1;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class AirPollutionSeoul_q1_Mapper extends Mapper<Object, Text, Text, FloatWritable>{

	Text station_code = new Text();
	FloatWritable output_PM10 = new FloatWritable();

	boolean is_head = true;

	protected void map(Object key, Text value, Mapper<Object, Text, Text, FloatWritable>.Context context)
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
				// set @station_code
				station_code.set(colums[1]);
				// set @ouput_PM10
				output_PM10.set(Float.parseFloat(colums[3]));
				// write context
				context.write(station_code, output_PM10);
			}
		}
	}
}
