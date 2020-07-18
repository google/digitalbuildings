package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IMakeup_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Makeup_water_valve_percentage_command;

/**
* Class Mwvpm 
* Make-up water valve percentage monitoring.
*/
@SuppressWarnings("serial")
public class Mwvpm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IMwvpm{

	IRI newInstance;
	public Mwvpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Mwvpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesMakeup_water_valve_percentage_command (IMakeup_water_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IMakeup_water_valve_percentage_command> getUsesMakeup_water_valve_percentage_command (){
		Set<IMakeup_water_valve_percentage_command> UsesMakeup_water_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Makeup_water_valve_percentage_command) {
				UsesMakeup_water_valve_percentage_command.add((Makeup_water_valve_percentage_command)action);
			}
		});
		return UsesMakeup_water_valve_percentage_command;
	}

	public static Set<IMwvpm> getAllMwvpmsObjectsCreated(){
		Set<IMwvpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Mwvpm")).subjects().stream()
		.map(mapper->(IMwvpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}