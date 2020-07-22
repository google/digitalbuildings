package example.rdf.digitalbuildings;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.Charset;

import org.eclipse.rdf4j.rio.RDFFormat;
import org.eclipse.rdf4j.rio.Rio;

import digitalbuildings.global.util.GLOBAL;
import www.google.com.digitalbuildings._0_0_1.facilities.Building;
import www.google.com.digitalbuildings._0_0_1.facilities.Floor;
import www.google.com.digitalbuildings._0_0_1.facilities.Room;
import www.google.com.digitalbuildings._0_0_1.fields.Dryer_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Run_status;
import www.google.com.digitalbuildings._0_0_1.hvac.Fan_ss;
import www.google.com.digitalbuildings._0_0_1.hvac.Fan_ss_dri;

public class Main {

	public static void main(String[] args) {
		createBuildingTopology();
		serialize();
	}

	public static void createBuildingTopology() {
		String exampleNamespace = "http://www.example.com/ont/tc2#";

		// Physical Location
		Building building = new Building(exampleNamespace, "12345");
		building.setCode("US-SVL-TC2");
		building.setFriendlyName("TC2 Building");

		Floor floor1 = new Floor(exampleNamespace, "floor1");
		floor1.setCode("US-SVL-TC2-1");

		Floor floor2 = new Floor(exampleNamespace, "floor2");
		floor2.setCode("US-SVL-TC2-2");

		Floor floor3 = new Floor(exampleNamespace, "floor3");
		floor3.setCode("US-SVL-TC2-3");

		Room room11 = new Room(exampleNamespace, "room11");
		room11.setCode("Room on floor 1");

		Room room21 = new Room(exampleNamespace, "room21");
		room21.setCode("Room on floor 2");

		Room room31 = new Room(exampleNamespace, "room31");
		room31.setCode("Room on floor 3");

		Room room32 = new Room(exampleNamespace, "room32");
		room32.setCode("Another Room on floor 3");

		// Connect Building and Floor
		building.addFloor(floor3);
		building.addFloor(floor2);
		building.addFloor(floor1);

		// Connect Room and Floor
		floor1.addRoom(room11);
		floor2.addRoom(room21);
		floor3.addRoom(room31);
		floor3.addRoom(room32);

		Fan_ss fan_ss1 = new Fan_ss(exampleNamespace, "fan_ss1");
		// Mandatory fields for fan ss
		Run_command runCommand = new Run_command(exampleNamespace, "rc1");
		runCommand.setTimeSeriesId("ts-1");

		Run_status runStatus = new Run_status(exampleNamespace, "rs1");
		runStatus.setTimeSeriesId("ts-2");

		// Connect Fields to commands
		fan_ss1.addUsesRun_command(runCommand);
		fan_ss1.addUsesRun_status(runStatus);

		// Add a location for the fan
		fan_ss1.addPhysicalLocation(room32);

		Fan_ss_dri fan_ss_dri1 = new Fan_ss_dri(exampleNamespace, "fan_ss_dri1");

		// Mandatory fields for fan mdri
		Run_command runCommand2 = new Run_command(exampleNamespace, "runCommand2");
		runCommand.setTimeSeriesId("ts-3");

		Run_status runStatus2 = new Run_status(exampleNamespace, "runStatus2");
		runStatus.setTimeSeriesId("ts-4");

		Dryer_run_status dryer_run_status = new Dryer_run_status(exampleNamespace, "dryer_run_status");
		dryer_run_status.setTimeSeriesId("ts-5");

		// Connect Fields to commands
		fan_ss_dri1.addUsesRun_command(runCommand2);
		fan_ss_dri1.addUsesRun_status(runStatus2);
		fan_ss_dri1.addUsesDryer_run_status(dryer_run_status);

		// Add a location for the fan
		fan_ss_dri1.addPhysicalLocation(room21);

	}

	public static void serialize() {
		ByteArrayOutputStream outStream = new ByteArrayOutputStream();

		Rio.write(GLOBAL.model, outStream, RDFFormat.JSONLD);

		String content = new String(outStream.toByteArray(), Charset.forName("UTF-8"));
		System.out.println(content);

		String fileName = "exampleOntologyInstance_TopologyConfig.rdf";
		File file = new File(fileName);

		try (FileOutputStream fos = new FileOutputStream(file.getName())) {
			fos.write(content.getBytes());
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
