package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_command;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_damper_command;

/**
* Class Oadm 
* Outside air damper monitoring.
*/
@SuppressWarnings("serial")
public class Oadm extends www.google.com.digitalbuildings._0_0_1.hvac.Functionality implements IOadm{

	IRI newInstance;
	public Oadm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Oadm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOutside_air_damper_command (IOutside_air_damper_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IOutside_air_damper_command> getUsesOutside_air_damper_command (){
		Set<IOutside_air_damper_command> UsesOutside_air_damper_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_damper_command) {
				UsesOutside_air_damper_command.add((Outside_air_damper_command)action);
			}
		});
		return UsesOutside_air_damper_command;
	}

	public static Set<IOadm> getAllOadmsObjectsCreated(){
		Set<IOadm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Oadm")).subjects().stream()
		.map(mapper->(IOadm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}