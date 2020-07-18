package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Bypass_air_damper_percentage_command;

/**
* Class Bypdm 
* Bypass damper monitoring.
*/
@SuppressWarnings("serial")
public class Bypdm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IBypdm{

	IRI newInstance;
	public Bypdm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Bypdm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesBypass_air_damper_percentage_command (IBypass_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBypass_air_damper_percentage_command> getUsesBypass_air_damper_percentage_command (){
		Set<IBypass_air_damper_percentage_command> UsesBypass_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Bypass_air_damper_percentage_command) {
				UsesBypass_air_damper_percentage_command.add((Bypass_air_damper_percentage_command)action);
			}
		});
		return UsesBypass_air_damper_percentage_command;
	}

	public static Set<IBypdm> getAllBypdmsObjectsCreated(){
		Set<IBypdm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Bypdm")).subjects().stream()
		.map(mapper->(IBypdm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}