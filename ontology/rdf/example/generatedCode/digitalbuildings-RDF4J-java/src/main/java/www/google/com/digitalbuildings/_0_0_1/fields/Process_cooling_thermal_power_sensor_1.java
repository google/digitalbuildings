package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.ICooling;
import www.google.com.digitalbuildings._0_0_1.subfields.Cooling;
import www.google.com.digitalbuildings._0_0_1.subfields.IProcess;
import www.google.com.digitalbuildings._0_0_1.subfields.Process;
import www.google.com.digitalbuildings._0_0_1.subfields.IPower;
import www.google.com.digitalbuildings._0_0_1.subfields.Power;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;
import www.google.com.digitalbuildings._0_0_1.subfields.Sensor;
import www.google.com.digitalbuildings._0_0_1.subfields.IThermal;
import www.google.com.digitalbuildings._0_0_1.subfields.Thermal;


@SuppressWarnings("serial")
public class Process_cooling_thermal_power_sensor_1 extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IProcess_cooling_thermal_power_sensor_1{

	IRI newInstance;
	public Process_cooling_thermal_power_sensor_1(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Process_cooling_thermal_power_sensor_1"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfCooling (ICooling parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ICooling> getComposedOfCooling (){
		Set<ICooling> ComposedOfCooling = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling) {
				ComposedOfCooling.add((Cooling)action);
			}
		});
		return ComposedOfCooling;
	}


  public void addComposedOfPower (IPower parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IPower> getComposedOfPower (){
		Set<IPower> ComposedOfPower = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Power) {
				ComposedOfPower.add((Power)action);
			}
		});
		return ComposedOfPower;
	}


  public void addComposedOfProcess (IProcess parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IProcess> getComposedOfProcess (){
		Set<IProcess> ComposedOfProcess = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Process) {
				ComposedOfProcess.add((Process)action);
			}
		});
		return ComposedOfProcess;
	}


  public void addComposedOfSensor (ISensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ISensor> getComposedOfSensor (){
		Set<ISensor> ComposedOfSensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Sensor) {
				ComposedOfSensor.add((Sensor)action);
			}
		});
		return ComposedOfSensor;
	}


  public void addComposedOfThermal (IThermal parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IThermal> getComposedOfThermal (){
		Set<IThermal> ComposedOfThermal = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Thermal) {
				ComposedOfThermal.add((Thermal)action);
			}
		});
		return ComposedOfThermal;
	}

	public static Set<IProcess_cooling_thermal_power_sensor_1> getAllProcess_cooling_thermal_power_sensor_1sObjectsCreated(){
		Set<IProcess_cooling_thermal_power_sensor_1> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Process_cooling_thermal_power_sensor_1")).subjects().stream()
		.map(mapper->(IProcess_cooling_thermal_power_sensor_1)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}