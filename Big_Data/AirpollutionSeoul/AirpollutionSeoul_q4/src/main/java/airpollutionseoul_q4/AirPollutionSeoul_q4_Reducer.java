package airpollutionseoul_q4;

import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class AirPollutionSeoul_q4_Reducer extends Reducer<Text, Text, Text, Text>{

	Text output_text = new Text();

	protected void reduce(Text key, Iterable<Text> values,
			Reducer<Text, Text, Text, Text>.Context context) throws IOException, InterruptedException {

		int total_SO2 = 0;
		float SO2 = 0;
		int total_NO2 = 0;
		float NO2 = 0;
		int total_CO = 0;
		float CO = 0;
		int total_O3 = 0;
		float O3 = 0;
		int total_PM10 = 0;
		float PM10 = 0;
		int total_PM2_5 = 0;
		float PM2_5 = 0;

		for(Text text : values) {
			// col[0] = item code, col[1] = Average value
			String[] col = text.toString().split(" ");
			switch (Integer.parseInt(col[0])){
				// SO2
				case 1:
					total_SO2 += 1;
					SO2 += Float.parseFloat(col[1]);
					break;
				// NO2
				case 3:
					total_NO2 += 1;
					NO2 += Float.parseFloat(col[1]);
					break;
				// CO
				case 5:
					total_CO += 1;
					CO += Float.parseFloat(col[1]);
					break;
				// O3
				case 6:
					total_O3 += 1;
					O3 += Float.parseFloat(col[1]);
					break;
				// PM10
				case 8:
					total_PM10 += 1;
					PM10 += Float.parseFloat(col[1]);
					break;
				// PM2.5
				case 9:
					total_PM2_5 += 1;
					PM2_5 += Float.parseFloat(col[1]);
					break;
			}
		}

		output_text.set(String.format("SO2: %f, NO2: %f, CO: %f, O3: %f, PM10: %f, PM2.5: %f",
				SO2/total_SO2, NO2/total_NO2, CO/total_CO, O3/total_O3, PM10/total_PM10, PM2_5/total_PM2_5));
		context.write(key, output_text);
		
	}

}
