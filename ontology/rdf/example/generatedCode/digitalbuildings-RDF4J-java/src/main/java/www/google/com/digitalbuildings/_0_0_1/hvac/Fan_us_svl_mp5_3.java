package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IDryer_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.Dryer_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDryer_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.Dryer_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IDryer_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Dryer_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDryer_run_status_5;
import www.google.com.digitalbuildings._0_0_1.fields.Dryer_run_status_5;
import www.google.com.digitalbuildings._0_0_1.fields.IDryer_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.Dryer_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.IDryer_run_status_7;
import www.google.com.digitalbuildings._0_0_1.fields.Dryer_run_status_7;
import www.google.com.digitalbuildings._0_0_1.fields.IDryer_run_status_6;
import www.google.com.digitalbuildings._0_0_1.fields.Dryer_run_status_6;
import www.google.com.digitalbuildings._0_0_1.fields.IDryer_run_status_8;
import www.google.com.digitalbuildings._0_0_1.fields.Dryer_run_status_8;

/**
* Class Fan_us_svl_mp5_3 
* Hash:baa9cc8812ae9b36bd430ca2574f7a3a5a003479d6623ff75573535ea8a3a467; Entities: US-SVL-MP5:FAN:EF 1-6
*/
@SuppressWarnings("serial")
public class Fan_us_svl_mp5_3 extends www.google.com.digitalbuildings._0_0_1.hvac.Fan_ss implements IFan_us_svl_mp5_3{

	IRI newInstance;
	public Fan_us_svl_mp5_3(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_svl_mp5_3"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesDryer_run_status_1 (IDryer_run_status_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDryer_run_status_1> getUsesDryer_run_status_1 (){
		Set<IDryer_run_status_1> UsesDryer_run_status_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Dryer_run_status_1) {
				UsesDryer_run_status_1.add((Dryer_run_status_1)action);
			}
		});
		return UsesDryer_run_status_1;
	}


  public void addUsesDryer_run_status_2 (IDryer_run_status_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDryer_run_status_2> getUsesDryer_run_status_2 (){
		Set<IDryer_run_status_2> UsesDryer_run_status_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Dryer_run_status_2) {
				UsesDryer_run_status_2.add((Dryer_run_status_2)action);
			}
		});
		return UsesDryer_run_status_2;
	}


  public void addUsesDryer_run_status_3 (IDryer_run_status_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDryer_run_status_3> getUsesDryer_run_status_3 (){
		Set<IDryer_run_status_3> UsesDryer_run_status_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Dryer_run_status_3) {
				UsesDryer_run_status_3.add((Dryer_run_status_3)action);
			}
		});
		return UsesDryer_run_status_3;
	}


  public void addUsesDryer_run_status_4 (IDryer_run_status_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDryer_run_status_4> getUsesDryer_run_status_4 (){
		Set<IDryer_run_status_4> UsesDryer_run_status_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Dryer_run_status_4) {
				UsesDryer_run_status_4.add((Dryer_run_status_4)action);
			}
		});
		return UsesDryer_run_status_4;
	}


  public void addUsesDryer_run_status_5 (IDryer_run_status_5 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDryer_run_status_5> getUsesDryer_run_status_5 (){
		Set<IDryer_run_status_5> UsesDryer_run_status_5 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Dryer_run_status_5) {
				UsesDryer_run_status_5.add((Dryer_run_status_5)action);
			}
		});
		return UsesDryer_run_status_5;
	}


  public void addUsesDryer_run_status_6 (IDryer_run_status_6 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDryer_run_status_6> getUsesDryer_run_status_6 (){
		Set<IDryer_run_status_6> UsesDryer_run_status_6 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Dryer_run_status_6) {
				UsesDryer_run_status_6.add((Dryer_run_status_6)action);
			}
		});
		return UsesDryer_run_status_6;
	}


  public void addUsesDryer_run_status_7 (IDryer_run_status_7 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDryer_run_status_7> getUsesDryer_run_status_7 (){
		Set<IDryer_run_status_7> UsesDryer_run_status_7 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Dryer_run_status_7) {
				UsesDryer_run_status_7.add((Dryer_run_status_7)action);
			}
		});
		return UsesDryer_run_status_7;
	}


  public void addUsesDryer_run_status_8 (IDryer_run_status_8 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDryer_run_status_8> getUsesDryer_run_status_8 (){
		Set<IDryer_run_status_8> UsesDryer_run_status_8 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Dryer_run_status_8) {
				UsesDryer_run_status_8.add((Dryer_run_status_8)action);
			}
		});
		return UsesDryer_run_status_8;
	}

	public static Set<IFan_us_svl_mp5_3> getAllFan_us_svl_mp5_3sObjectsCreated(){
		Set<IFan_us_svl_mp5_3> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_svl_mp5_3")).subjects().stream()
		.map(mapper->(IFan_us_svl_mp5_3)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}