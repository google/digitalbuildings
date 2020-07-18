package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IBoost_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Boost_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IBoost_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Boost_fan_run_command;

/**
* Class Bfss 
* Booster fan start-stop and feedback.
*/
@SuppressWarnings("serial")
public class Bfss extends www.google.com.digitalbuildings._0_0_1.Operational implements IBfss{

	IRI newInstance;
	public Bfss(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Bfss"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesBoost_fan_run_command (IBoost_fan_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBoost_fan_run_command> getUsesBoost_fan_run_command (){
		Set<IBoost_fan_run_command> UsesBoost_fan_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Boost_fan_run_command) {
				UsesBoost_fan_run_command.add((Boost_fan_run_command)action);
			}
		});
		return UsesBoost_fan_run_command;
	}


  public void addUsesBoost_fan_run_status (IBoost_fan_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBoost_fan_run_status> getUsesBoost_fan_run_status (){
		Set<IBoost_fan_run_status> UsesBoost_fan_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Boost_fan_run_status) {
				UsesBoost_fan_run_status.add((Boost_fan_run_status)action);
			}
		});
		return UsesBoost_fan_run_status;
	}

	public static Set<IBfss> getAllBfsssObjectsCreated(){
		Set<IBfss> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Bfss")).subjects().stream()
		.map(mapper->(IBfss)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}