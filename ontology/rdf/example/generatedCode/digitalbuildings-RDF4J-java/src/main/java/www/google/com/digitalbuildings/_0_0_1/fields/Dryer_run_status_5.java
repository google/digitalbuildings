package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.Status;
import www.google.com.digitalbuildings._0_0_1.subfields.IRun;
import www.google.com.digitalbuildings._0_0_1.subfields.Run;
import www.google.com.digitalbuildings._0_0_1.subfields.IDryer;
import www.google.com.digitalbuildings._0_0_1.subfields.Dryer;


@SuppressWarnings("serial")
public class Dryer_run_status_5 extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IDryer_run_status_5{

	IRI newInstance;
	public Dryer_run_status_5(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Dryer_run_status_5"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfDryer (IDryer parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IDryer> getComposedOfDryer (){
		Set<IDryer> ComposedOfDryer = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Dryer) {
				ComposedOfDryer.add((Dryer)action);
			}
		});
		return ComposedOfDryer;
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

	public static Set<IDryer_run_status_5> getAllDryer_run_status_5sObjectsCreated(){
		Set<IDryer_run_status_5> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Dryer_run_status_5")).subjects().stream()
		.map(mapper->(IDryer_run_status_5)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}