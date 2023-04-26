package airpollutionseoul_q1;

import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class AirPollutionSeoul_q1_Reducer extends Reducer<Text, FloatWritable, Text, Text>{

	Text output_key = new Text();
	Text output_text = new Text();

	protected void reduce(Text key, Iterable<FloatWritable> values,
			Reducer<Text, FloatWritable, Text, Text>.Context context) throws IOException, InterruptedException {

		int total_data = 0;
		float total_pm10 = 0;
		float avg_pm10 = 0;
		float max_pm10 = 0;
		float min_pm10 = 0;
		float tmp_pm10 = 0;

		for(FloatWritable PM10 : values) {

			total_data += 1;
			total_pm10 += PM10.get();
			tmp_pm10 = PM10.get();

			if(tmp_pm10 > max_pm10){
				max_pm10 = tmp_pm10;
			}
			// At first, @min_pm = @tmp_pm10
			if (min_pm10 == 0) {
				min_pm10 = tmp_pm10;
			}

			if (tmp_pm10 < min_pm10) {
				min_pm10 = tmp_pm10;
			}

		}
		avg_pm10 = total_pm10/total_data ;
		output_key.set("station code = " + key);
		output_text.set(String.format("avg: %f, max: %f, min: %f",avg_pm10, max_pm10, min_pm10));
		context.write(output_key, output_text);
		
	}

}
