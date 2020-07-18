package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.Status;
import www.google.com.digitalbuildings._0_0_1.subfields.IHeater;
import www.google.com.digitalbuildings._0_0_1.subfields.Heater;
import www.google.com.digitalbuildings._0_0_1.subfields.IRun;
import www.google.com.digitalbuildings._0_0_1.subfields.Run;


@SuppressWarnings("serial")
public class Heater_run_status extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IHeater_run_status{

	IRI newInstance;
	public Heater_run_status(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Heater_run_status"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfHeater (IHeater parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IHeater> getComposedOfHeater (){
		Set<IHeater> ComposedOfHeater = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Heater) {
				ComposedOfHeater.add((Heater)action);
			}
		});
		return ComposedOfHeater;
	}


  public void addComposedOfRun (IRun parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IRun> getComposedOfRun (){
		Set<IRun> ComposedOfRun = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Run) {
				ComposedOfRun.add((Run)action);
			}
		});
		return ComposedOfRun;
	}


  public void addComposedOfStatus (IStatus parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IStatus> getComposedOfStatus (){
		Set<IStatus> ComposedOfStatus = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Status) {
				ComposedOfStatus.add((Status)action);
			}
		});
		return ComposedOfStatus;
	}

	public static Set<IHeater_run_status> getAllHeater_run_statussObjectsCreated(){
		Set<IHeater_run_status> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Heater_run_status")).subjects().stream()
		.map(mapper->(IHeater_run_status)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}